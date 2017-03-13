# coding=utf-8

class LXUser:
    def __init__(self):
        self.user = {}

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
