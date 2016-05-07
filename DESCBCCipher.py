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
      plaintext += chr(ord('0'))                            # Add 0 (character) as a pad
    plaintext += chr(ord(str(padLength)))                   # Append number of bytes padded to end of plaintext (can be anywhere in range 1-7).

    return plaintext

  def encrypt(self,plaintext,IV):
    if len(plaintext) % DES.block_size is not 0:            # Check if the final plaintext block fits into 8 bytes (64 bits).
      plaintext = self.pad(plaintext)                       # Pad the plaintext (if required)
    DESCBCkey = self._key                                   # Set the key
    encipher = DES.new(DESCBCkey)                           # Create new DESCBC object with given key in CBC mode
    ciphertext = ""			                                    # ciphertext will hold the encrypted plaintext

    IV_in_bits = strToBinStr(IV)                            # Convert the IV from string to binary string (64 bits)

    n = 8                                                   # Use this value (8) to split the plaintext into blocks of 8 bytes
    plaintext_in_blocks = [plaintext[i:i+n] for i in range(0, len(plaintext), n)] # Create a list of these plaintext blocks

    plaintext_in_bits = strToBinStr(plaintext_in_blocks[0]) # Convert the first 8-byte plaintext block to 64-bit binary for xor
    current_block_xor = bin(int(plaintext_in_bits, 2) ^ int(IV_in_bits, 2))[2:] # xor the first block and the IV, cut off the '0b' at the front
    if (len(current_block_xor) < 64):                       # Check if the binary string needs padding of 0's at the front    
      current_block_xor = ("0" * (8 - (len(current_block_xor) % 8))) + current_block_xor # Prepend missing 0's if needed since the xor removes 0's in the front
    
    first_block_str = binStrToStr(current_block_xor)        # Convert the xored binary string to a string, which is now ready to be encrypted
    cipher_block = encipher.encrypt(first_block_str)        # The first block has been processed and is encrypted here; keep this string for xoring
    ciphertext += cipher_block                              # ciphertext keeps the total string combination of all cipher_blocks

    for block in plaintext_in_blocks[1:]:                   # Loop through all blocks of plaintext except the first block, which has already been done
      plaintext_in_bits = strToBinStr(block)                # Convert the current block from string to binary
      cipher_in_bits = strToBinStr(cipher_block)            # Convert the cipher_block from string to binary
      current_block_xor = bin(int(plaintext_in_bits, 2) ^ int(cipher_in_bits, 2))[2:] # xor the current block and the previous cipher_block, cut off the '0b' at the front
      if (len(current_block_xor) < 64):                     # Check if the binary string needs padding of 0's at the front
        current_block_xor = ("0" * (8 - (len(current_block_xor) % 8))) + current_block_xor # Prepend missing 0's if needed since the xor removes 0's in the front
      current_block_str = binStrToStr(current_block_xor)    # Convert the xored binary string to a string, which is now ready to be encrypted
      cipher_block = encipher.encrypt(current_block_str)    # The current block has been processed and is encrypted here; keep this string for xoring
      ciphertext += cipher_block                            # Add the encrypted text to the ciphertext

    return ciphertext                                       # Return the completed ciphertext, which is our enciphered result

  def decrypt(self,ciphertext,IV): 
    DESCBCkey = self._key                                   # Set the key
    decipher = DES.new(DESCBCkey)                           # Create new DESCBC object with given key in CBC mode
    plaintext = ""									                        # plaintext will hold the decrypted ciphertext

    n = 8                                                   # Use this value (8) to split the ciphertext into blocks of 8 bytes
    ciphertext_in_blocks = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)] # Create a list of these ciphertext blocks

    ciphertext_decrypted = decipher.decrypt(ciphertext_in_blocks[0]) # Decrypt the first ciphertext block
    ciphertext_in_bits = strToBinStr(ciphertext_decrypted)  # Convert this decrypted ciphertext block from string into binary
    
    IV_in_bits = strToBinStr(IV)                            # Convert the IV from string to binary
    current_block_xor = bin(int(ciphertext_in_bits, 2) ^ int(IV_in_bits, 2))[2:] # xor the first ciphertext_in_bits and the IV_in_bits
    if (len(current_block_xor) < 64):                       # Check if the binary string needs padding of 0's at the front
      current_block_xor = ("0" * (8 - (len(current_block_xor) % 8))) + current_block_xor # Prepend missing 0's if needed since the xor removes 0's in the front
    plaintext += binStrToStr(current_block_xor)             # Convert the xored block result from binary to string, and append to the plaintext

    i = 0                                                   # Keep track of the previous ciphertext block
    for block in ciphertext_in_blocks[1:]:                  # Loop through all blocks of plaintext except the first block, which has already been done
      ciphertext_decrypted = decipher.decrypt(block)        # Decrypt the current block
      ciphertext_in_bits = strToBinStr(ciphertext_decrypted)# Convert the current decrypted ciphertext from string to binary 
      prev_ciphertext_in_bits = strToBinStr(ciphertext_in_blocks[i]) # Convert the previous ciphertext from string to binary
      current_block_xor = bin(int(ciphertext_in_bits, 2) ^ int(prev_ciphertext_in_bits, 2))[2:] # xor the current decrypted ciphertext and the previous ciphertext block
      if (len(current_block_xor) < 64):                     # Check if the binary string needs padding of 0's at the front
        current_block_xor = ("0" * (8 - (len(current_block_xor) % 8))) + current_block_xor # Prepend missing 0's if needed since the xor removes 0's in the front
      plaintext += binStrToStr(current_block_xor)           # Convert the xored block result from binary to string, and append to the plaintext
      i += 1                                                # Increase the counter to go to the next ciphertext block.
      
    return plaintext                                        # Return the completed plaintext, which is our deciphered result
