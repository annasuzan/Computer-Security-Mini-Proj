# A-Simple-Ransomware-in-Python

1. Create two VMs having Linux OS, one that acts as the attacker and the other the victim.
2. Generate the RSA public and private key by running the keygen.py file on the attacker’s machine.
python3 keyGen.py
3. Keep an HTTP server running on the attacker's machine.
python3 -m http.server 9000
4. Start server.py at the attacker's machine.
python3 server.py
5. Run client.py as a background process on the victim's machine.
python3 client.py &
6. Once the ransomware note starts popping up, send EMAIL_ME.txt to the attacker via email.
7. Attacker decrypts the AES key by running dec_aesKey.py.
python3 dec_aesKey.py
8. The decrypt AES key is stored in the file dec_aesKey.txt. Send this over to the victim.
9. Place the dec_aesKey.txt file inside the infected folder and wait for the files to be decrypted.