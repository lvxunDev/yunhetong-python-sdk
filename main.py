from lx_user import LXUser

if __name__ == "__main__":
    user = LXUser()
    u = {
        'appId': "2016121514373700002",
        'appUserId': 'phpTestUserB',
        'userType': 1,
        'cellNum': '11111111122',
        'userName': 'TestB',
        'certifyType': 2,
        'certifyNumber': '52059487',
        'createSignature': '0'
    }
    public = '/pem/yhtSK.pem'
    private = '/pem/rsa_private_key_pkcs8.pem'

    create_user = user.set_user(u)
    if create_user:
        user_a = user.get_user()
        sdk_manager = user.get_lx_sdk_manager(public, private)
        print sdk_manager.get_token(user_a)
    else:
        print create_user
