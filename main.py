import json

from SDKManager import SDKManager
from LXUser import LXUser

if __name__ == "__main__":
    user = LXUser()
    userA = user.getUserA()
    # userA = user.getUserB()
    SDKManagerByUser = user.getLxSDKManager()
    a = SDKManagerByUser.sync_get_token(userA)
    for i in a:
        print a[i]

