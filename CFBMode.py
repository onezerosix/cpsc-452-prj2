'''
  IV is going to be an 8 character string
  s is int in terms of bits
  example of binary string: '100111010101010' (any length)
  example of string: 'k12lk~!^&HDF(*lkj*DSF(9.,'
  
  example runs:
  python CipherDriver.py DESCFB 1234567890abcdef ENC long.txt out.txt 01234567 3
  python CipherDriver.py DESCFB 1234567890abcdef DEC out.txt out2.txt 01234567 3
  python CipherDriver.py RSACFB pubkey.pem ENC long.txt out.txt iviviviv 10
  python CipherDriver.py RSACFB privkey.pem DEC out.txt out2.txt iviviviv 10
'''

from DESCipher import DESCipher
from RSACipher import RSACipher
from binaryStrings import *

def encryptCFB(cipher, plaintext, IV, s):
  ciphertext = '' 
  shiftreg = strToBinStr(IV)
  plaintext = strToBinStr(plaintext)
  if len(plaintext)%s != 0:
    plaintext += '0' * (s - (len(plaintext) % s))  # pad plaintext if needed

  for i in range(len(plaintext) / s):
    temp = strToBinStr(cipher.encrypt(binStrToStr(shiftreg))) # encrypt shiftreg

    # xor s bits of SR with plaintext block, result is binStr (no '0b')
    cipherblock = bin(int(temp[:s], 2) ^ int(plaintext[i*s:(i+1)*s], 2))[2:]

    cipherblock = ('0' * (s - len(cipherblock))) + cipherblock # prepend missing 0s if needed
    shiftreg = shiftreg[s:64] + cipherblock # shift SR and put cipherblock in
    ciphertext += cipherblock

  return binStrToStr(ciphertext)


def decryptCFB(cipher, ciphertext, IV, s):
  plaintext = ''
  shiftreg = strToBinStr(IV)
  ciphertext = strToBinStr(ciphertext)

  # if ciphertext isn't divisible by s, strToBinStr put extra padding or s is wrong
  trimLastByte(ciphertext, s)
  
  for i in range(len(ciphertext) / s):
    temp = strToBinStr(cipher.encrypt(binStrToStr(shiftreg))) # encrypt shiftreg

    # xor s bits of SR with plaintext block, result is binStr (no '0b')
    plaintextblock = bin(int(temp[:s], 2) ^ int(ciphertext[i*s:(i+1)*s], 2))[2:]

    plaintextblock = ('0' * (s - len(plaintextblock))) + plaintextblock # prepend missing 0s
    shiftreg = shiftreg[s:64] + ciphertext[i*s:(i+1)*s] # shift SR and put cipherblock in
    plaintext += plaintextblock

  return binStrToStr(plaintext)
