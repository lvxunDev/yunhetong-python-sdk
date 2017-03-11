import base64
import json
import time
from Crypto.Cipher import AES
from Crypto import Random


class aes:
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
        size = 16  # (MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC) block size
        data = self._pad(data, 16)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.secretKey, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(data))

    def decrypt(self, dataB):
        data = base64.b64decode(dataB)
        cipher = AES.new(self.secretKey, AES.MODE_CBC, self.iv)
        res = cipher.decrypt(data)
        return self._unpad(res).decode('utf-8')

    def toString(self):
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
        self.bt = 1234567890123

    def _pad(self, s, block_size):
        pad = block_size - (len(s) % block_size)
        return s + pad * chr(pad)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
