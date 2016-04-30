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
    # key is stored inside a file (public or private)
    # store key: self._key = RSA.importKey(f.read())
    return False

  def encrypt(self,plaintext):
    # encrypt with help of Crypto library
    # self._key.encrypt(<plaintext>, 32) # 32 might be wrong, according to documentation, it's a random number
    return "enciphered"

  def decrypt(self,ciphertext):
    # decrypt with help of Crypto library
    # self._key.decrypt(<ciphertext>)
    return "deciphered"


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
