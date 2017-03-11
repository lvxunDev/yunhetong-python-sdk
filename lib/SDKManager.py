import json
import requests

from secretManager import secretManager


class SDKManager:
    def __init__(self, appId, pubPath, priPath):
        self.host = "http://sdk.yunhetong.com/sdk"
        # self.host = "http://localhost:8080/sdk"
        self.appId = appId
        self.pubPath = pubPath
        self.priPath = priPath
        self.secretManager = secretManager(self.appId, self.pubPath, self.priPath)

    def encrypt(self, data):
        return self.secretManager.encrypt(data)

    def sync_get_token(self, user):
        url = "/third/tokenWithUser"
        current_user = {"currentUser": user}
        secret = self.secretManager.encrypt(json.dumps(current_user))
        data = {
            'appid': self.appId,
            'secret': secret
        }

        # data = {
        #     'appid': self.appId,
        #     'secret': '{"key":"YYGTUhX5XVcTsaz8oaMZCo6R7qU1DR6zPSMRT9vUXK6nKnFaeSkoEfoIj9XIKzyFuGDVQv55zTCeKD5vtffKihCWg4F5R9gNhtv1AInx7bhzg27BY609We9zzWRigqkOP3lNueviBywa\/OB90Mv4ljuZ+gQTHtetozAVMNNNSH0=","content":"m3ztNK6b6chJpv4q6y61y7Y+GCNIt0wEUSh\/snLBInTo6r7rc6mcPBNye6jU3PI361R3lAJo9Cb9cKlbVV12w7avxWLJ4NyuFUrs97QUJi1IcnRWHDaP9w2vVB3BMiGcdd\/OD6qt+V7ugec7RfM4xm\/3upePH9+F1Bq3iRJO5S42LEJEtmCMLEvC3lpIS8W4mB2NhxSPuXmiFOzFNckrE478hxQl\/WrNoK9IsfV5lXx\/MM7O+r65N1TQNwUP3PmjTpZwL4xxuNVz5uLzh5X\/6g==","sign":"wSUXdmDf+EeKlJCRxNnWlPHSl\/eV+2xbOAcjDTcXt4RuhGa84BT2NP+j6cEqihN3jBYVdg4wwBRt3Buge7MLS4wJXZ\/6rKwgisD4soDbdYZv\/lGoK+4L4PpZ1nV\/SstdKX4SpYd1z1RXNj+33f+iTndcQITfN5Na1f\/tmiYtaXqbWk+KPR9P89STTn0FL5AQ7olIF1vrj0kuF5rq41MFRcROTzdwY4ebwZ1nztOODsc="}'
        # }

        r = requests.post(self.host + url, data)

        return self.secretManager.decrypt(r.json())
