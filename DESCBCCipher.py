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

  # Padding format used: 0's followed by number of padded bytes.
  #   ex:   Last block of plaintext = "cat"
  #         Padded = "cat00005"
  def pad(self,plaintext):
    padLength = DES.block_size - (len(plaintext) % DES.block_size) # Calculate how many bytes must be padded

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

    IV_in_bits = strToBinStr(IV)

    n = 8
    plaintext_in_blocks = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]  # Loop through plaintext and split in blocks of 8 bytes (64 bits)

    #plaintext_in_bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in plaintext_in_blocks[0])
    plaintext_in_bits = strToBinStr(plaintext_in_blocks[0]) # Convert plaintext string to binary for xor
    current_block_xor = bin(int(plaintext_in_bits, 2) ^ int(IV_in_bits, 2))[2:]
    current_block_xor = ("0" * (8 - (len(current_block_xor) % 8))) + current_block_xor # prepend missing 0s if needed 
    first_block_str = binStrToStr(current_block_xor)
   
    cipher_block = encipher.encrypt(first_block_str)
    ciphertext += cipher_block

    for block in plaintext_in_blocks[1:]:                   # Loop through all blocks of plaintext except the first block
      plaintext_in_bits = ''.join('{0:08b}'.format(ord(x), 'b') for x in block)
      cipher_in_bits = strToBinStr(cipher_block)
      current_block_xor = bin(int(plaintext_in_bits, 2) ^ int(cipher_in_bits, 2))[2:]
      current_block_str = binStrToStr(current_block_xor)
      cipher_block = encipher.encrypt(current_block_str)
      ciphertext += cipher_block

    return ciphertext

  def decrypt(self,ciphertext,IV): 
    DESCBCkey = self._key                                   # Set the key
    decipher = DES.new(DESCBCkey)                           # Create new DESCBC object with given key in CBC mode
    plaintext = ""									                        # plaintext will hold the decrypted ciphertext

    n = 8
    ciphertext_in_blocks = [decipher.decrypt(ciphertext[i:i+n]) for i in range(0, len(ciphertext), n)]
    ciphertext_in_bits = strToBinStr(ciphertext_in_blocks[0])


    #TODO: currently does not work.
    IV_in_bits = strToBinStr(IV)

    xored = bin(int(ciphertext_in_bits, 2) ^ int(IV_in_bits, 2))[2:]
    print(xored)

    xored_str = binStrToStr(xored)

    print(xored_str)

    #plaintext = decipher.decrypt(ciphertext)			          # Decrypt the ciphertext and store it in the plaintext string
		
    return plaintext                                        # Return the plaintext, which is our deciphered result

