# should we hard code s?

#def strToBinStr(myS):
#  myL = []
#  for i in range(len(myS)):
#    x = bin(ord(myS[i]))[2:]
#    x = ('0' * (8 - (len(x) % 8))) + x
#    myL.append(x)
#  ''.join(myL)
  
#def binStrToStr(myB):
#  myS = ''
#  for i in range(0, len(myB), 8):
#    myS += chr(int(myB[i:i+8], 2))


def encryptCFB(cipher, plaintext, IV):
  initialvector = '0123456789abcdef'
  s=16
  ciphertext = '' 
  shiftreg = strToBinStr(initialvector)
  plaintext = strToBinStr(plaintext)
  plaintext += '0' * (s - (len(plaintext) % s))
  
  for i in range(len(plaintext) / s):
    out = strToBinStr(cipher.encrypt(binStrToStr(shiftreg)))
    cipherblock = int(out[:s], 2) ^ int(plaintext[i*s:(i+1)*s], 2)
    ciphertext += binStrToStr(cipherblock)
    shiftreg = shiftreg[s:64] + cipherblock
