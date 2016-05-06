"""
CPSC 452
Assignment 2
DES Cipher Class in CBC Mode

Programmer: Eric Roe
Python 2.7

Required Files: CipherInterface.py

This class utilizes uses the CipherInterface class to perform
encryption and decryption with the DES class from the pyCrpto library.



To install pyCrypto on linux/Ubuntu :
  $pip install pycrypto
"""

from Crypto.Cipher import DES
from Crypto import Random 	                                # Will potentially be used with IV for other Block Cipher modes
from CipherInterface import CipherInterface
import string

def strToBinStr(myS):
  myL = []
  for i in range(len(myS)):
    x = bin(ord(myS[i]))[2:] # i-th char in myS to int to binary & strip '0b' (gets a binary string)
    pad_to_8 = len(x) % 8
    if pad_to_8 is not 0:
      x = (8 - pad_to_8) * "0" + x
    myL.append(x)
  return ''.join(myL)
  
def binStrToStr(myB):
  myS = ''
  for i in range(0, len(myB), 8):
    myS += chr(int(myB[i:i+8], 2))
  return myS

class DESCBCCipher (CipherInterface):
  __slots__ ={'_key'}
  
  # Default initialization
  def __init__(self):
    self._key = None

  def setKey(self,key):
    if len(key) is 16 and all(char in string.hexdigits for char in key):  # Check that the key is 16 hexidecimal characters
      key = str(bytearray.fromhex(key))                     # Change the key to a byte array (Crypto library requires 8 byte input)
      self._key = key                                       # Set the encryption/decryption key
      return True                                           # key is valid and successfully set
    else:
      return False                                          # key is invalid and rejected

  def pad(self,plaintext):
    padLength = DES.block_size - (len(plaintext) % DES.block_size) # Calculate how many bytes must be padded
                                                            # Padding format used: 0's followed by number of padded bytes.
                                                            #   ex:   Last block of plaintext = "cat"
                                                            #         Padded = "cat00005"
    for i in range(padLength -1):                           # Append (padLength - 1) 0's to the plaintext.
      plaintext += chr(0)
    plaintext += chr(padLength)                             # Append number of bytes padded to end of plaintext (can hold values 1-7).

    return plaintext






  def encrypt(self,plaintext,IV):
    if len(plaintext) % DES.block_size is not 0:            # Check if the final plaintext block fits into 8 bytes (64 bits).
      plaintext = self.pad(plaintext)                       # Pad the plaintext (if required)
    DESCBCkey = self._key                                   # Set the key
    encipher = DES.new(DESCBCkey)                           # Create new DESCBC object with given key in CBC mode
    ciphertext = ""			                                    # ciphertext will hold the encrypted plaintext

    #print("IV: {}".format(IV))

    #IV_ready2 = str(bytearray.fromhex(IV))
    #IV_in_bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in IV_ready2) # Convert plaintext string to binary for xor

    IV_in_bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in IV)

    IV_in_bits = strToBinStr(IV)

    #print("IV_in_bits:\n{}".format(IV_in_bits))
    #print("IV_in_bits SIZE: {}".format(len(IV_in_bits)))

    n = 8
    plaintext_in_parts = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]

    #ciphertext += encipher.encrypt(first_block)
    plaintext_in_bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in plaintext_in_parts[0]) # Convert plaintext string to binary for xor

    #print("plaintext_in_bits:\n{}".format(plaintext_in_bits))
    plaintext_back = binStrToStr(plaintext_in_bits)

    #print("plaintext_back: {}".format(plaintext_back))

    first_block = bin(int(plaintext_in_bits, 2) ^ int(IV_in_bits, 2))[2:]
    first_block = ("0" * (8 - (len(first_block) % 8))) + first_block # prepend missing 0s if needed 
    #print("RESULT:\n{}".format(first_block))

    first_block_str = binStrToStr(first_block)
    #print("RESULT 2:\n{}".format(first_block_str))
    #for block in plaintext_in_parts:
    #  print(block)

    #TODO: After the xor, encrypt the data. Convert it back to a non-binary format.
    #TODO: Loop through all parts of the plaintext instead of just the first block.

    return 0
    #ciphertext += encipher.encrypt(plaintext)               # Encrypt the plaintext and store it in the ciphertext string

    #return ciphertext                                       # Return the ciphertext, which is our enciphered result



















  def decrypt(self,ciphertext,IV): 
    DESCBCkey = self._key                                   # Set the key
    descipher = DES.new(DESCBCkey)                           # Create new DESCBC object with given key in CBC mode
    plaintext = ""									                        # plaintext will hold the decrypted ciphertext

    

    plaintext = decipher.decrypt(ciphertext)			          # Decrypt the ciphertext and store it in the plaintext string
		
    return plaintext                                        # Return the plaintext, which is our deciphered result


def encryptCFB(cipher, plaintext, IV, s):
  #TODO: ALL (will be working on it tomorrow during a 3 hr break)
  ciphertext = '' 
  shiftreg = strToBinStr(IV)
  #print shiftreg, " and it's type is ", type(shiftreg)
  plaintext = strToBinStr(plaintext)

