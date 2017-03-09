import base64
import json
import time
from Crypto.Cipher import AES
from Crypto import Random


class aes:
    def __init__(self, key=''):
        if '' != key:
            self.key = json.loads(key)
            self.secretKey = self.key['key']
            self.iv = self.key['iv']
            self.bt = self.key['bt']
        else:
            self.refresh()

    def encrypt(self, data):
        size = ''
        data = data
        return 'encrypt'

    def toString(self):
        missing_padding = 4 - len(self.iv) % 4
        if missing_padding:
            self.iv += b'=' * missing_padding

        ret_map = {
            'key': unicode(base64.b64encode(self.secretKey), errors='ignore'),
            'content': unicode(base64.b64decode(self.iv), errors='ignore'),
            'sign': unicode(base64.b64decode(self.bt), errors='ignore')
        }
        return json.dumps(ret_map)

    def refresh(self):
        self.iv = Random.new().read(AES.block_size)
        # todo create key generator
        self.secretKey = '1234567812345678'  # SeanWu told me to write this
        self.bt = str(time.time() * 1000)
