import json
import requests

from secretManager import secretManager


class SDKManager:
    def __init__(self, appId, pubPath, priPath):
        self.host = "http://sdk.yunhetong.com/sdk"
        self.appId = appId
        self.pubPath = pubPath
        self.priPath = priPath
        self.secretManager = secretManager(self.appId, self.pubPath, self.priPath)

    def encrypt(self, data):
        return self.secretManager.encrypt(data)

    def sync_get_token(self, user):
        url = "/third/tokenWithUser"
        current_user = {"currentUser": user}
        secret = self.secretManager.encrypt(json.dumps(current_user))
        data = {
            'appid': self.appId,
            'secret': secret
        }
        r = requests.post(self.host + url, data)
        print r.json()
