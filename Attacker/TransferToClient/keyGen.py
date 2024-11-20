import os
import base64
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Random import get_random_bytes

file_extensions = [".txt"]
    
def keyGenRSA():
    #generates master RSA key
    print("Generating master key...")

    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    
    print("Master key generated. Writing to files...\n")
    pubKey = key.publickey().exportKey('PEM')
    privKey = key.exportKey('PEM')

    with open('pubKey.pem', 'wb') as f:
        f.write(pubKey)

    with open('privKey.pem', 'wb') as f:
        f.write(privKey)

    print("Your public key is: ")
    print("(n, e) : ({}, {})".format(key.n, key.e))
    #   print("masterkey = RSA.importKey(base64.b64decode(b\"{}\"))".format(base64.b64encode(key.publickey().exportKey()).decode()))
    
    return key


def keyGenSymmetric():
    # generates symmetric keys to encrypt files using Salsa20 stream cipher
    print("\nGenerating symmetric keys...")
    
    salsakeys = []
    for ext in file_extensions:
        # salsakey = Random.new().read(2) + 30 * b'/x00'
        salsakey = get_random_bytes(32)
        salsakeys.append(salsakey)
    print("Salsakeys: {}".format(salsakeys))
    
    return salsakeys

if __name__ == "__main__":
    keyGenRSA()

    # keyGenSymmetric()