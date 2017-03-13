# coding=utf-8
from aes import Aes
from rsa import rsa
import json


class SecretManager:
    """
    SecretManager构造函数
    设置appId 创建对应的aes、rsa
    :param appId:    第三方应用的appId
    :param pubPath:  公钥地址
    :param priPath:  私钥地址
    """

    def __init__(self, appId, pubPath, priPath):
        self.appId = appId
        self.aes = Aes()
        self.rsa = rsa(pubPath, priPath)

    def encrypt(self, jsonData):
        """
        加密方法
        :param jsonData: 需要加密的data
        :return:         json封装过的加密完毕的信息
        """
        key = self.rsa.encryptAES(self.aes)
        content = self.aes.encrypt(jsonData)
        sign = self.aes.encrypt(self.sign_data(jsonData))
        ret_map = {'key': key, 'content': content, 'sign': sign}
        return json.dumps(ret_map)

    def decrypt(self, jsonData):
        """
        解密方法
        :param jsonData: 需要解密的data
        :return:         解密后的信息或是报错信息
        """
        try:
            session_key = jsonData['key']
            session_key = self.rsa.decryptRSA(session_key)
            aes_handler = Aes(session_key)
            return aes_handler.decrypt(jsonData['content'])
        except:
            return jsonData

    def sign_data(self, data):
        """
        签名方法
        :param data:   需要rsa签名的data
        :return:       rsa签名完毕的字符串
        """
        return self.rsa.sign_data(data)
