from LXUser import LXUser

if __name__ == "__main__":
    user = LXUser()
    userA = user.getUserA()
    SDKManagerByUser = user.getLxSDKManager()
    a = SDKManagerByUser.sync_get_token(userA)
    print a

