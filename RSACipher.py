"""
CPSC 452
Assignment 2
RSA Cipher Class

Python 2.7

Required Files: Cipherinterface.py

This class utilizes uses the CipherInterface class to perform
encryption and decryption with the RSA class from the pyCrpto library.

To generate and save keys:
key = RSA.generate(<size in bits>)
# open a file
  f.write(RSA.exportKey('PEM'))

example run:
python CipherDriver.py RSA ekey.pem ENC long.txt out.txt
python CipherDriver.py RSA dkey.pem DEC out.txt out2.txt
"""
from Crypto.PublicKey import RSA
from CipherInterface import CipherInterface
import sys

class RSACipher (CipherInterface):
  def __init__(self):
    self._key = None

  def setKey(self,key):
    # key is stored inside a file (public or private)
    success = False
    try:
      with open(key) as f:
        self._key = RSA.importKey(f.read())                   # self._key is now an _RSA Object
        success = True
    except IOError:
      print "ERROR: could not open file: " + key
    except ValueError:
      print "ERROR: could not import key"
  
    # if importing was successful but cannot encrypt or decrypt
    if success and not(self._key.has_private() or self._key.can_encrypt()):
      success = False
      print "ERROR: your key can't encrypt or decrypt"
      
    return success

  def encrypt(self,plaintext):
    # encrypt with help of Crypto library
    # self._key.encrypt(<plaintext>, 32) # 32 might be wrong, according to documentation, it's a random number
    enciphered = ""
    blocks = []
    temp = 0
    maxSize = 256 #(self._key.size()/8) +1 # maximum size of text that the key can handle in bytes


    for i in range(len(plaintext)/maxSize):                     # For every block, block cannot be larger than maxSize
      blocks.append(plaintext[i*maxSize:(i+1)*maxSize])         # Split the plaintext into blocks
      temp = i + 1                                              # Save the block counter in case there is an extra block to encrypt
    if range(len(plaintext)%maxSize != 0):                      # Check if there is a remaining block
      blocks.append(plaintext[temp*maxSize:(temp+1)*maxSize])   # If there is, append the remaining bytes
    cipherBlocks = []                                           # Initialized empty list of cipher blocks
    for i in range(len(blocks)):                                # For each block of plaintext, encrypt the block
      try:
#        print len(blocks[i])
        oneCipherBlock = self._key.encrypt(blocks[i], 32)[0]
      except ValueError:
        print "ERROR: couldn't process a block"
        sys.exit(-1)
      while len(oneCipherBlock) < maxSize:
        oneCipherBlock = "\x00" + oneCipherBlock
      cipherBlocks.append(oneCipherBlock)  # Note: Pycrypto's RSA always returns a tuple, with the 2nd item being None
    enciphered = "".join(cipherBlocks)                          # Concatinate the encrypted blocks into a string
    return enciphered                                           # Return the ciphered text

  def decrypt(self,ciphertext):
    # decrypt with help of Crypto library
    # self._key.decrypt(<ciphertext>)
    deciphered = ""
    maxSize = 256 #(self._key.size()/8)+1 # maximum size of text that the key can handle in bytes
    
    if self._key.has_private() == False: # can't decrypt with public key
      print "ERROR: Can't decrypt without a private key\nCheck README"
      sys.exit(-1)
    
    else:
      blocks = []                                           # Initialized empty list of blocks to decrypt
      temp = 0                                              # in case of an imperfect size
      for i in range(len(ciphertext)/maxSize):              # For every block, block cannot be larger maxSize
        blocks.append(ciphertext[i*maxSize:(i+1)*maxSize])  # Split the ciphertext into blocks
        temp = i + 1                                        # Save the block counter in case there is an extra block
      if range(len(ciphertext)%maxSize != 0):               # Check if there is a remaining block
        blocks.append(ciphertext[temp*maxSize:(temp+1)*maxSize])    # If there is, append the remaining bytes to the block
      decipherBlocks = []                                   # Initialized empty list of deciphered blocks
      for i in range(len(blocks)):                          # For each block of ciphertext, encrypt the block
        try:
          decipherBlocks.append(self._key.decrypt(blocks[i])) # Note: RSAObj's decryption function doesn't return a tuple like encrypt
        except ValueError:
          print "ERROR: couldn't process a block"
          sys.exit(-1)
      deciphered = "".join(decipherBlocks)                  # Concatinate the decrypted blocks into a string
    return deciphered                                       # Return the deciphered text

