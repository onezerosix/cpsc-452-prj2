"""
CPSC 452
Assignment 1
Cipher Interface Base Class
"""

class CipherInterface:
  __slots__ = {'_key'}
  
  def __init__(self, key):
    self._key = None

  def setKey(self, key):
    self._key = key

  def encrypt(self, plaintext):
    return None

  def decrypt(self, ciphertext):
    return None
