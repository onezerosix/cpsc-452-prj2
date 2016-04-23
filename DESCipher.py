"""
CPSC 452
Assignment 2
DES Cipher Class

Programmer: Alejandro Sanchez
Python 2.7

Required Files: Cipherinterface.py

This class utilizes uses the CipherInterface class to perform
encryption and decryption with the DES class from the pyCrpto library.



To install pyCrpto on linux/Ubuntu :

$pip install pycrypto
"""

from Crypto.Cipher import DES
from Crypto import Random 	#will potentially be used with IV for other Block Cipher modes
from CipherInterface import CipherInterface
import string

class DESCipher (CipherInterface):
	__slots__ ={'_key'}
  
  #Default initialization
	def __init__(self):
		self._key = None
    	self._padFlag = 0  #Keep track of whether or not plaintext was padded before encryption 0 = no, 1 = yes

	def setKey(self,key):
		if len(key) is 8 and all(character in string.hexdigits for character in key):  # If the key length is 16 (8 bytes) and contains only Hexadecimal characters
			self._key = key                # Set the encryption/decryption key
			return True                    # Return True, Key successfully set
		else:								# Otherwise...
			return False                    # The Key is invalid
	def encrypt(self,plaintext):
		DESkey = self._key   #set decryption key to key passed as parameter
		enciphered = ""			# encrypted plaintext
		cipher = DES.new(DESkey) # Create new DES object with given key, default mode is ECB mode
		
	# Check if plaintext perfectly fits into 64 bit blocks
		if len(plaintext)% DES.block_size is not 0:	# if it doesn't	
			self._padFlag = 1;						# then set the padFlag to 1, indicating that the plaintext is padded
			padLength = DES.block_size - (len(plaintext) % DES.block_size) #generate padding for plaintext with bytes of 0's followed by the number of bytes added. i.e. 003 or 0004
			for i in range(padLength -1):  # append padding of 0's to plaintext before encryption
				plaintext += chr(0)
			plaintext += chr(padLength)    #append number of bytes padded to end of plaintext

		enciphered = cipher.encrypt(plaintext) #create ciphertext

		return enciphered

	def decrypt(self,ciphertext): 
		DESkey = self._key 								  #set decryption key to key passed as parameter
		deciphered = ""									# decrypted ciphertext
		cipher = DES.new(DESkey)						 # Create new DES object with given key, default mode is ECB mode
		deciphered = cipher.decrypt(ciphertext)			 # decrpyt given ciphertext using DES object from Crypto library
	# Check if plaintext was padded before ecnryption
		#if self._padFlag is 1: 							# If plaintext was padded
		#	lastIndex = deciphered[-1].encode("hex")	# obtain last nibble from decrypted ciphertext and convert to hex representation
			#print ("last index in deciphered: ", int(lastIndex,16)) #Print decimal value of last index
		#	deciphered = deciphered[:(len(deciphered) - int(lastIndex,16))] #Display plaintext without the padded bytes
		#	self._padFlag= 0 							#reset _padFlag to 0
		
		return deciphered