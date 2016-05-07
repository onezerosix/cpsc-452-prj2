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
from CipherInterface import CipherInterface
import string

class DESCipher (CipherInterface):
  __slots__ ={'_key'}
  
  # Default initialization
  def __init__(self):
    self._key = None

  def setKey(self,key):
    success = False
    if len(key) is 16 and all(char in string.hexdigits for char in key):  # Check that the key is 16 hexidecimal characters
      convertedKey = ''
      try:
        for i in range(0,16,2): # change every 2 hex digits to 1 character
          iByte = int(key[i:i+2], 16)
          convertedKey += chr(iByte)
        success = True
      except ValueError:
        print "ERROR: error occured while converting 16 digit key to one 8 byte value"

    if success and len(convertedKey) == 8: # key converted correctly
      self._key = convertedKey                                       # Set the encryption/decryption key
    else:
      print self._key
      success = False
    return success

  # Padding format used: 0's followed by number of padded bytes.
  #   ex:   Last block of plaintext = "cat"
  #         Padded = "cat00005"
  def pad(self,plaintext):
    padLength = DES.block_size - (len(plaintext) % DES.block_size) # Calculate how many bytes must be padded

    for i in range(padLength -1):                           # Append (padLength - 1) 0's to the plaintext.
      plaintext += chr(ord('0'))                            # Add 0 (character) as a pad
    plaintext += chr(ord(str(padLength)))                   # Append number of bytes padded to end of plaintext (can be anywhere in range 1-7).

    return plaintext

  def encrypt(self,plaintext):
    DESkey = self._key                                      # Set the key
    ciphertext = ""			                                    # ciphertext will hold the encrypted plaintext
    encipher = DES.new(DESkey)                              # Create new DES object with given key, which defaults to ECB mode
		
    if len(plaintext) % DES.block_size is not 0:            # Check if the final plaintext block fits into 8 bytes (64 bits).
      plaintext = pad(plaintext)

    ciphertext = encipher.encrypt(plaintext)                # Encrypt the plaintext and store it in the ciphertext string

    return ciphertext                                       # Return the ciphertext, which is our enciphered result

  def decrypt(self,ciphertext): 
    DESkey = self._key 								                      # Set the key
    plaintext = ""									                        # plaintext will hold the decrypted ciphertext
    decipher = DES.new(DESkey)						                  # Create new DES object with given key, which defaults to ECB mode
    plaintext = decipher.decrypt(ciphertext)			          # Decrypt the ciphertext and store it in the plaintext string
		
    return plaintext                                        # Return the plaintext, which is our deciphered result
