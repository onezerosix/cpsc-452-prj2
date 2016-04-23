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

class RASCipher (CipherInterface):
  def __init__(self):
    self._key = None

  def setKey(self,key):
    # key is stored inside a file (public or private)
    # store key: self._key = RSA.importKey(f.read())

  def encrypt(self,plaintext):
    # encrypt with help of Crypto library
    # self._key.encrypt(<plaintext>, 32) # 32 might be wrong, according to documentation, it's a random number
    return "enciphered"

  def decrypt(self,ciphertext):
    # decrypt with help of Crypto library
    # self._key.decrypt(<ciphertext>)
    return "deciphered"
