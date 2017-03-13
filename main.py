# coding=utf-8
from lib.lx_user import LXUser
from resouse import R

if __name__ == "__main__":
    # 首先，初始化 sdk_manager
    sdk_manager = R.get_sdk_manager()
    # 然后随便初始化一个用户信息
    user_a = R.get_test_user_a()
    # 获取这个用户的 token
    print sdk_manager.get_token(user_a) + '\r\n\r\n'
    # 创建一份合同
    print sdk_manager.create_contract(R.get_test_contract(), R.get_actors()) + '\r\n\r\n'
    # 或者你也可以在创建合同的时候顺便获取 token
    print sdk_manager.token_contract(R.get_test_user_a(), R.get_test_contract(), R.get_actors()) + '\r\n\r\n'
    # 查询合同列表
    print sdk_manager.query_contracts(10, 1) + '\r\n\r\n'
