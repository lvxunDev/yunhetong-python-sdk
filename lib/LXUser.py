from SDKManager import SDKManager


class LXUser:
    def __init__(self):
        # self.appId = "2016121514373700002"
        self.appId = "2016082413581300000"

    def getLxSDKManager(self):
        # return SDKManager(self.appId, '/pem2/yhtSK.pem', '/pem2/rsa_private_key_pkcs8.pem')
        return SDKManager(self.appId, '/pem/yhtSK.pem', '/pem/rsa_private_key_pkcs8.pem')

    def getUserA(self):
        user = {
            'appId': self.appId,
            'appUserId': 'phpTestUserA1',
            'userType': 1,
            'cellNum': '',
            'userName': 'TestA',
            'certifyType': 2,
            'certifyNumber': '52059487',
            'createSignature': '0'
        }
        return user

    def getUserB(self):
        user = {
            'appId': self.appId,
            'appUserId': 'javaTestUserCA9',
            'userType': 1,
            'cellNum': '15267132222',
            'userName': 'TestB',
            'certifyType': 1,
            'certifyNumber': '123',
            'createSignature': '0'
        }
        return user
