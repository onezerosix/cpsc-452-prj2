# IV is going to be an 8 character string
# s is int in terms of bits

from DESCipher import DESCipher
from RSACipher import RSACipher

def strToBinStr(myS):
  myL = []
  for i in range(len(myS)):
    x = bin(ord(myS[i]))[2:] # i-th char in myS to int to binary & strip '0b' (gets a binary string)
    if len(x) != 8:
      x = ('0' * (8 - (len(x) % 8))) + x # prepend missing 0s if needed
    myL.append(x)
  return ''.join(myL)
  
def binStrToStr(myB):
  myS = ''
  for i in range(0, len(myB), 8):
    myS += chr(int(myB[i:i+8], 2))
  return myS

def encryptCFB(cipher, plaintext, IV, s):
  ciphertext = '' 
  shiftreg = strToBinStr(IV)
  plaintext = strToBinStr(plaintext)
  plaintext += '0' * (s - (len(plaintext) % s))  # pad plaintext if needed

  for i in range(len(plaintext) / s):
    out = strToBinStr(cipher.encrypt(binStrToStr(shiftreg)))
    cipherblock = bin(int(out[:s], 2) ^ int(plaintext[i*s:(i+1)*s], 2))[2:] # xor s bits of SR with plaintext block, result is binStr (no '0b')
    if len(cipherblock) != s:
      cipherblock = ('0' * (s - (len(cipherblock) % s))) + cipherblock # prepend missing 0s if needed
    shiftreg = shiftreg[s:64] + cipherblock # shift SR and put cipherblock in
    ciphertext += binStrToStr(cipherblock)
    print len(plaintext[i*s:(i+1)*s]), " ", len(cipherblock)
  return ciphertext


def decryptCFB(cipher, ciphertext, IV, s):
  plaintext = '' 
  shiftreg = strToBinStr(IV)
  ciphertext = strToBinStr(ciphertext)
  ciphertext += '0' * (s - (len(ciphertext) % s))  # pad ciphertext if needed

  for i in range(len(ciphertext) / s):
    out = strToBinStr(cipher.encrypt(binStrToStr(shiftreg)))
    plaintextblock = bin(int(out[:s], 2) ^ int(ciphertext[i*s:(i+1)*s], 2))[2:] # xor s bits of SR with plaintext block, result is binStr (no '0b')
    if len(plaintextblock) != s:
      plaintextblock = ('0' * (s - (len(plaintextblock) % s))) + plaintextblock # prepend missing 0s if needed
    shiftreg = shiftreg[s:64] + ciphertext[i*s:(i+1)*s] # shift SR and put cipherblock in
    print len(plaintextblock), " ", len(ciphertext[i*s:(i+1)*s])
    plaintext += binStrToStr(plaintextblock)
  return plaintext
