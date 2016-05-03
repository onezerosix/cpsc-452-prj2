#IV is going to be a 16 character string
# s is in bits

from DESCipher import DESCipher
from RSACipher import RSACipher

def strToBinStr(myS):
  myL = []
  for i in range(len(myS)):
    x = bin(ord(myS[i]))[2:] # i-th char in myS to int to binary & strip '0b' (gets a binary string)
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
  #print shiftreg, " and it's type is ", type(shiftreg)
  plaintext = strToBinStr(plaintext)
  plaintext += '0' * (s - (len(plaintext) % s))  # pad plaintext if needed

  for i in range(len(plaintext) / s):
    out = strToBinStr(cipher.encrypt(binStrToStr(shiftreg)))
    cipherblock = bin(int(out[:s], 2) ^ int(plaintext[i*s:(i+1)*s], 2))[2:] # xor s bits of SR with plaintext block, result is binStr (no '0b')
    cipherblock = ('0' * (8 - (len(cipherblock) % 8))) + cipherblock # prepend missing 0s if needed 
    shiftreg = shiftreg[s:64] + cipherblock # shift SR and put cipherblock in
    ciphertext += binStrToStr(cipherblock)
    print "plainblock ", len(plaintext[i*s:(i+1)*s]), "cipherblock ", len(cipherblock)
  return ciphertext


def decryptCFB(cipher, ciphertext, IV, s):
  plaintext = '' 
  shiftreg = strToBinStr(IV)
  ciphertext = strToBinStr(ciphertext)
  ciphertext += '0' * (s - (len(ciphertext) % s))  # pad ciphertext if needed

  for i in range(len(ciphertext) / s):
    out = strToBinStr(cipher.encrypt(binStrToStr(shiftreg)))
    plaintextblock = bin(int(out[:s], 2) ^ int(ciphertext[i*s:(i+1)*s], 2))[2:] # xor s bits of SR with plaintext block, result is binStr (no '0b')
    plaintextblock = ('0' * (8 - (len(plaintextblock) % 8))) + plaintextblock # prepend missing 0s if needed
    shiftreg = shiftreg[s:64] + ciphertext[i*s:(i+1)*s] # shift SR and put cipherblock in
    plaintext += binStrToStr(plaintextblock)
    print "plainblock ", len(plaintextblock), "cipherblock ", len(ciphertext[i*s:(i+1)*s])
  return plaintext







