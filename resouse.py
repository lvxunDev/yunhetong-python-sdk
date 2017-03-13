# coding=utf-8
import time

from lib.lx_user import LXUser
from lib.sdk_manager import SDKManager


class R:

    app_id = "2016121514373700002"
    pub_path = '/pem/yhtSK.pem'
    pri_path = '/pem/rsa_private_key_pkcs8.pem'
    #app_id = "2016082413581300000"
    #pub_path = '/pem/local/yhtSK.pem'
    #pri_path = '/pem/local/rsa_private_key_pkcs8.pem'


    @staticmethod
    def get_sdk_manager():
        """
            get a test SDKManager
        """
        return SDKManager(R.app_id, R.pub_path, R.pri_path)

    @staticmethod
    def get_test_user_a():
        user_a = {
            'appId': R.app_id,
            'appUserId': 'pythonTestUserA',
            'userType': 1,
            'cellNum': '11111111122',
            'userName': 'TestB',
            'certifyType': 2,
            'certifyNumber': '52059487',
            'createSignature': '0'
        }
        return user_a

    @staticmethod
    def get_test_user_b():
        user_b = {
            'appId': R.app_id,
            'appUserId': 'pythonTestUserB',
            'userType': 1,
            'cellNum': '11111111122',
            'userName': 'TestB',
            'certifyType': 2,
            'certifyNumber': '52059487',
            'createSignature': '0'
        }
        return user_b

    @staticmethod
    def get_test_contract():
        contract = {
            "appId" : R.app_id,
            "title" : "测试合同标题",
            "overtime" : int(round(time.time() * 1000)),
            "defContractNo" : "自定义合同标题",
            "templateId" : 123456,
            "params" : R.get_contract_params(),
        }
        return contract

    @staticmethod
    def get_contract_params():
        params = {
            "${nameA}" : "py测试用户名A"
        }
        return params


    @staticmethod
    def get_actors():
        return (R.actor_a(),R.actor_b())


    @staticmethod
    def actor_a():
        actor_a = {
            "user" : R.get_test_user_a(),
            "locationName" : "signA",
            "autoSign" : 0
        }
        return actor_a


    @staticmethod
    def actor_b():
        actor_b = {
            "user" : R.get_test_user_b(),
            "locationName" : "signA",
            "autoSign" : 0
        }
        return actor_b

