"""
CPSC 452
Assignment 2
DES Cipher Class

Programmer: Alejandro Sanchez
Modified 4/23/16: Eric Roe
Python 2.7

Required Files: Cipherinterface.py

This class utilizes uses the CipherInterface class to perform
encryption and decryption with the DES class from the pyCrpto library.



To install pyCrypto on linux/Ubuntu :
  $pip install pycrypto
"""

from Crypto.Cipher import DES
from Crypto import Random 	                                # Will potentially be used with IV for other Block Cipher modes
from CipherInterface import CipherInterface
import string

class DESCipher (CipherInterface):
  __slots__ ={'_key'}
  
  # Default initialization
  def __init__(self):
    self._key = None
    self._padFlag = 0                                       # Keep track of whether or not plaintext was padded before encryption; 0 = no, 1 = yes

  def setKey(self,key):
    if len(key) is 16 and all(char in string.hexdigits for char in key):  # Check that the key is 16 hexidecimal characters
      key = str(bytearray.fromhex(key))                     # Change the key to a byte array (Crypto library requires 8 byte input)
      self._key = key                                       # Set the encryption/decryption key
      return True                                           # key is valid and successfully set
    else:
      return False                                          # key is invalid and rejected

  def encrypt(self,plaintext):
    DESkey = self._key                                      # Set the key
    ciphertext = ""			                                    # ciphertext will hold the encrypted plaintext
    encipher = DES.new(DESkey)                              # Create new DES object with given key, which defaults to ECB mode
		
    if len(plaintext) % DES.block_size is not 0:            # Check if the final plaintext block fits into 8 bytes (64 bits).
      self._padFlag = 1;						                        # Set padFlag to 1, indicating that we are padding the plaintext.

      padLength = DES.block_size - (len(plaintext) % DES.block_size) # Calculate how many bytes must be padded
                                                            # Padding format used: 0's followed by number of padded bytes.
                                                            #   ex:   Last block of plaintext = "cat"
                                                            #         Padded = "cat00005"
      for i in range(padLength -1):                         # Append (padLength - 1) 0's to the plaintext.
        plaintext += chr(0)
      plaintext += chr(padLength)                           # Append number of bytes padded to end of plaintext (can hold values 1-7).

    ciphertext = encipher.encrypt(plaintext)                # Encrypt the plaintext and store it in the ciphertext string

    return ciphertext                                       # Return the ciphertext, which is our enciphered result

  def decrypt(self,ciphertext): 
    DESkey = self._key 								                      # Set the key
    plaintext = ""									                        # plaintext will hold the decrypted ciphertext
    decipher = DES.new(DESkey)						                  # Create new DES object with given key, which defaults to ECB mode
    plaintext = decipher.decrypt(ciphertext)			          # Decrypt the ciphertext and store it in the plaintext string
		
    return plaintext                                        # Return the plaintext, which is our deciphered result
