# coding=utf-8
from sdk_manager import SDKManager


class LXUser:
    def __init__(self):
        self.user = {}

    def get_lx_sdk_manager(self, public, private):
        """
        获取sdk manager方法
        :param public:   公钥地址
        :param private:  私钥地址
        :returns:        SDKManager
        """
        return SDKManager(self.user['appId'], public, private)

    def get_user(self):
        """
        获取user方法
        :returns:user 字典
        """
        return self.user

    def set_user(self, u):
        """
        设置user方法
        :param u: 用户信息字典
        :returns: true 或是异常信息
        """
        try:
            self.user = u
            return True
        except Exception, e:
            return e
