# coding=utf-8
import json
import requests

from secretManager import SecretManager


class SDKManager:
    """
    SDKManager构造函数
    设置初始变量并构造一个对应的secretManager
    :param appId:    第三方应用的appId
    :param pubPath:  公钥地址
    :param priPath:  私钥地址
    """

    def __init__(self, appId, pubPath, priPath):
        self.host = 'http://sdk.yunhetong.com/sdk'
        self.appId = appId
        self.pubPath = pubPath
        self.priPath = priPath
        self.secretManager = SecretManager(self.appId, self.pubPath, self.priPath)

    def get_token(self, user):
        """
        获取token的方法
        加密数据并做一个post请求
        :param user:   用户信息
        :returns:      请求回调信息
        """
        url = '/third/tokenWithUser'
        current_user = {'currentUser': user}
        secret = self.secretManager.encrypt(json.dumps(current_user))
        data = {
            'appid': self.appId,
            'secret': secret
        }
        r = requests.post(self.host + url, data)

        return self.secretManager.decrypt(r.json())
