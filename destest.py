'''
FILE: destest.py
PyVERSION:  2.7

TO RUN PROGRAM:  $python destest

DESCRIPTION: Test program for DESCipher class

FILES REQUIRED: CipherInterface.py
				DESCipher.py

PYTHON LILBRARIES REQUIRED : pycrpyto

				$pip install pycrpyto

'''

from CipherInterface import CipherInterface
from DESCipher import DESCipher

myDES = DESCipher()
key = raw_input ("Enter the key: ")

if myDES.setKey(key) == False:
	 print("Invalid key for DES Block Cipher. Key must be 8 Byte Hexadecimal value")

else:
	 
	msg = raw_input ("Enter the message: ")
	print ("The key is: " , myDES._key)
	out = myDES.encrypt(msg)
	print ("Ciphertext: ")
	print (out)
	decrypted = myDES.decrypt(out)
	print ("Plaintext: ")
	print (decrypted)