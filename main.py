import json

from SDKManager import SDKManager
from LXUser import LXUser

if __name__ == "__main__":
    user = LXUser()
    userA = user.getUserA()
    SDKManagerByUser = user.getLxSDKManager()

    SDKManagerByUser.sync_get_token(json.dumps(userA))

