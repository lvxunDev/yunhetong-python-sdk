# coding=utf-8
import base64
import json
import time
from Crypto.Cipher import AES
from Crypto import Random


class Aes:
    """
    aes构造函数
    如果有key传入，就调用该key，如果没有，就设置一个新key
    :param key:key字典，包含aes加密需要的 secretKey iv bt
    """

    def __init__(self, key=''):
        self.bs = 16
        if '' != key:
            self.key = json.loads(key)
            self.secretKey = base64.b64decode(self.key['key'])
            self.iv = base64.b64decode(self.key['iv'])
            self.bt = self.key['bt']
        else:
            self.refresh()

    def encrypt(self, data):
        """
        aes加密方法
        :param data: 需要加密的数据
        :return:     加密完毕的数据
        """
        data = self._pad(data, 16)
        cipher = AES.new(self.secretKey, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(data))

    def decrypt(self, data):
        """
        aes解密方法
        :param data: 需要解密的数据
        :return:     解密完毕的数据
        """
        data64 = base64.b64decode(data)
        cipher = AES.new(self.secretKey, AES.MODE_CBC, self.iv)
        res = cipher.decrypt(data64)
        return self._unpad(res).decode('utf-8')

    def to_string(self):
        """
        加密信息转字符串方法
        :return: json字符串
        """
        self.iv += "=" * ((4 - len(self.iv) % 4) % 4)

        ret_map = {
            'key': base64.b64encode(self.secretKey),
            'iv': base64.b64encode(self.iv),
            'bt': self.bt
        }
        return json.dumps(ret_map)

    def refresh(self):
        self.iv = Random.new().read(AES.block_size)
        # todo create key generator
        self.secretKey = '1234567812345678'  # SeanWu told me to write this
        self.bt = int(round(time.time() * 1000))

    @staticmethod
    def _pad(s, block_size):
        pad = block_size - (len(s) % block_size)
        return s + pad * chr(pad)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
