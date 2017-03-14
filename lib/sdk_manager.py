# coding=utf-8
import json
import requests
import time

from secretManager import SecretManager


class SDKManager:


    def __init__(self, app_id, pub_path, pri_path):
        self.host = 'http://sdk.yunhetong.com/sdk'
        # self.host = 'http://localhost:8080/sdk'
        self.app_id = app_id
        self.pub_path = pub_path
        self.pri_path = pri_path
        self.secret_manager = SecretManager(
            self.app_id, self.pub_path, self.pri_path)

    def get_token(self, user):
        """
        获取token的方法
        加密数据并做一个post请求
        :param user:   用户信息
        :returns:      返回该用户对应的 Token
        """
        url = '/third/tokenWithUser'
        current_user = {'currentUser': user}
        secret = self.secret_manager.encrypt(json.dumps(current_user))
        data = {
            'appid': self.app_id,
            'secret': secret
        }
        response = requests.post(self.host + url, data)
        return self.secret_manager.decrypt(response.json())

    def create_contract(self, contract, actors):
        """
        创建合同的方法
        加密数据并做一个post请求
        :param contract:   合同信息
        :param actors:     合同参与方信息
        :returns:      请求回调信息
        """
        url = '/third/autoContract'
        contract_form_vo = {'vo': contract, 'attendUser': actors}
        contract_info = {"contractFormVo": contract_form_vo}
        secret = self.secret_manager.encrypt(json.dumps(contract_info))
        data = {
            'appid': self.app_id,
            'secret': secret
        }
        response = requests.post(self.host + url, data)
        return self.secret_manager.decrypt(response.json())

    def token_contract(self, current_user, contract, actors):
        """
        创建合同并获取Token的方法
        :param current_user 要获取token的用户
        :param 合同信息
        :param 合同参与方信息
        :returns:      合同 id 和相应的 token
        """
        url = '/third/tokenWithContract'
        contract_form_vo = {'vo': contract, 'attendUser': actors}
        contract_info = {"currentUser": current_user,
                         "contractFormVo": contract_form_vo}
        secret = self.secret_manager.encrypt(json.dumps(contract_info))
        data = {
            'appid': self.app_id,
            'secret': secret
        }
        response = requests.post(self.host + url, data)
        return self.secret_manager.decrypt(response.json())

    def query_contracts(self, page_size, page_num):
        """
        查询合同列表
        :param 每页的数量
        :param 要查的页数
        :returns:    相应的合同列表
        """
        url = '/third/listContract'
        query_param = {'flag': int(round(time.time() * 1000)),
                       'pageSize': 10 if page_size < 10 else page_size,
                       'pageNum': 1 if page_num < 1 else page_num
                       }
        secret = self.secret_manager.encrypt(json.dumps(query_param))
        data = {
            'appid': self.app_id,
            'secret': secret
        }
        response = requests.post(self.host + url, data)
        return self.secret_manager.decrypt(response.json())

    def invalid_contract(self, contract_id):
        """
        作废合同
        :param 要作废的合同id
        """
        url = '/third/invalidContract'
        query_param = {'contractId': contract_id,
                       'timestamp': int(round(time.time() * 1000))
                       }
        secret = self.secret_manager.encrypt(json.dumps(query_param))
        data = {
            'appid': self.app_id,
            'secret': secret
        }
        response = requests.post(self.host + url, data)
        return self.secret_manager.decrypt(response.json())

    def get_last_notice(self):
        """
        获取最后一次消息的接口
        由于消息回调的方法本地不好调试，我们添加了一个获取最后一次消息的接口，方便本地调试
        使用方法：在完成合同操作之后，调用这个方法去获取我们服务端发的消息，然后再处理直接拿到消息模拟消息回调的过程。
        """
        url = '/third/getLastNotice'
        data = {
            'appid': self.app_id
        }
        response = requests.get(self.host + url, data)
        return self.secret_manager.decrypt(response.json())

    def sign_data(self, data):
        """
        对与合同发来的签署信息进行签名
        :param 云合同传过来的参数
        return 消息签名之后的数据
        """
        content = json.loads(data)
        # 1时表示普通合同签署
        if content["noticeType"] == 1:
            return json.dumps({'response': True, 'msg': 'ok'})
        elif content["noticeType"] == 2:  # 2时表示合同签署完成
            sign = self.secret_manager.sign_data(content["signDigest"])
            ret_dict = {
                'response': True,
                'msg': 'ok',
                'signDigest': self.secret_manager.encrypt(json.dumps(sign))
            }
            return self.secret_manager.decrypt(json.load(ret_dict))
        else:
            ret_dict = {"response": False, 'msg': u'不是签署成功的合同的数据，不需要签名!'}
            return json.dumps(ret_dict)
