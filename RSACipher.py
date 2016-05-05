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
"""
from Crypto.PublicKey import RSA
from Crypto import Random
from CipherInterface import CipherInterface
import string

class RSACipher (CipherInterface):
  def __init__(self):
    self._key = None

  def setKey(self,key):
    # key is stored inside a file (public or private)f
    # store key: self._key = RSA.importKey(f.read())
    success = False
    with open(key) as f:
      self._key = RSA.importKey(f.read())                   # self._key is now an _RSA Object
      if (self._key):
        success = True
    return success

  def encrypt(self,plaintext):
    # encrypt with help of Crypto library
    # self._key.encrypt(<plaintext>, 32) # 32 might be wrong, according to documentation, it's a random number
    enciphered = ""
    blocks = []
    temp = 0
    for i in range(len(plaintext)/256):                     # For every block, block cannot be larger than the modulus 256
      blocks.append(plaintext[i*256:(i+1)*256])             # Split the plaintext into blocks
      temp = i + 1                                          # Save the block counter in case there is an extra block to encrypt
    if range(len(plaintext)%256 != 0):                      # Check if there is a remaining block
      blocks.append(plaintext[temp*256:(temp+1)*256])       # If there is, append the remaining bytes
    cipherBlocks = []                                       # Initialized empty list of cipher blocks
    for i in range(len(blocks)):                                # For each block of plaintext, encrypt the block
      cipherBlocks.append(self._key.encrypt(blocks[i], 32)[0])  # Note: Pycrypto's RSA always returns a tuple, with the 2nd item being None
    enciphered = "".join(cipherBlocks)                          # Concatinate the encrypted blocks into a string
    return enciphered                                           # Return the ciphered text

  def decrypt(self,ciphertext):
    # decrypt with help of Crypto library
    # self._key.decrypt(<ciphertext>)
    deciphered = ""
    try:                                                    # Checks if the key is a private key
      blocks = []                                           # Initialized empty list of blocks to decrypt
      temp = 0                                              # in case of an imperfect size
      for i in range(len(ciphertext)/256):                  # For every block, block cannot be larger than the modulus 256
        blocks.append(ciphertext[i*256:(i+1)*256])          # Split the ciphertext into blocks
        temp = i + 1                                        # Save the block counter in case there is an extra block
      if range(len(ciphertext)%256 != 0):                   # Check if there is a remaining block
        blocks.append(ciphertext[temp*256:(temp+1)*256])    # If there is, append the remaining bytes to the block
      decipherBlocks = []                                   # Initialized empty list of deciphered blocks
      for i in range(len(blocks)):                          # For each block of ciphertext, encrypt the block
        decipherBlocks.append(self._key.decrypt(blocks[i])) # Note: RSAObj's decryption function doesn't return a tuple like encrypt
      deciphered = "".join(decipherBlocks)                  # Concatinate the decrypted blocks into a string
    except TypeError:                                       # If a public key is used to decrypt, RSA returns an error
      deciphered = "TypeError: This version of RSA can only decrypt using a private key"
    return deciphered                                       # Return the deciphered text


""" 2 versions
import rsa
from rsa import key, common
(pubKey, privKey) = rsa.newkeys(512, accurate=True) # 512 is max key size, for project need to import key, not generate
with open('things-changed.txt') as f:
  text = f.read()
blocks = []
for i in range(len(text)/53): # can only handle < 54 bytes at a time
  blocks.append(text[i*53:(i+1)*53])
cipherBlocks = []
for i in range(len(blocks)):
  cipherBlocks.append(rsa.encrypt(blocks[i],pubKey))
decrypted = []
for i in range(len(cipherBlocks)):
  decrypted.append(rsa(cipherBlocks[i], privKey))
# can encrypt with privKey but can't decrypt with pubKey

from Crypto.PublicKey import RSA
with open('pubkey.pem') as f:
  pubKey = RSA.importKey(f.read())
with open('privkey.pem') as f:
  privKey = RSA.importKey(f.read())
with open('README.txt') as f:
  text = f.read()
cipherBlock = pubKey.encrypt(text[:256], 32) # only handles < 257 bytes at a time, 32 is random int
decryptedBlock = privKey.decrypt(cipherBlock)
# can encrypt with privKey but can't decrypt with pubKey
"""
