from aes import aes
from rsa import rsa
import json

# todo rename class

class secretManager:
    def __init__(self, appId, pubPath, priPath):
        self.appId = appId
        self.aes = aes()
        self.rsa = rsa(pubPath, priPath)

    def encrypt(self, jsonData):
        key = self.rsa.encryptAES(self.aes)
        content = self.aes.encrypt(jsonData)
        sign = self.aes.encrypt(self.sign_data(jsonData))
        ret_map = {'key': key, 'content': content, 'sign': sign}
        return json.dumps(ret_map)

    def sign_data(self, data):
        return self.rsa.sign_data(data)
