import base64
import sys
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5


class rsa:
    def __init__(self, pubPath, priPath):
        path = sys.path[0]
        with open(path + pubPath) as publicFile:
            self.pubKey = publicFile.read()
        with open(path + priPath) as privateFile:
            self.priKey = privateFile.read()

    def encryptAES(self, aes):
        base_pub = base64.b64decode(self.pubKey)
        rsa_key = RSA.importKey(base_pub)
        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        aes_str = aes.toString()
        return base64.b64encode(cipher.encrypt(aes_str))

    def decryptRSA(self, data):
        base_pri = base64.b64decode(self.priKey)
        rsa_key = RSA.importKey(base_pri)
        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        random = ''  # what's this!!!
        return cipher.decrypt(base64.b64decode(data), random)

    def sign_data(self, data):
        key = base64.b64decode(self.priKey)

        private_key = RSA.importKey(key)
        hash_obj = SHA.new(data)
        signer = PKCS1_v1_5.new(private_key)
        return base64.b64encode(signer.sign(hash_obj))
