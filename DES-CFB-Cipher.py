#Questions:
#Is plaintext binary?
#Is initialvector binary?

# We are hardcoding the iv = '12345678' for now as well as the s-bits

def strToBinStr(myS):
  myL = []
  for i in range(len(myS)):
    x = bin(ord(myS[i]))[2:]
    x = ('0' * (8 - (len(x) % 8))) + x
    myL.append(x)
  ''.join(myL)
  
def binStrToStr(myB):
  myS = ''
  for i in range(0, len(myB), 8):
    myS += chr(int(myB[i:i+8], 2))


def encryptCFB(des, plaintext):
  initialvector = '0123456789abcdef'
  s=16
  ciphertext = '' 
  shiftreg = strToBinStr(initialvector)
  plaintext = strToBinStr(plaintext)
  plaintext += '0' * (s - (len(plaintext) % s))
  
  for i in range(len(plaintext) / s):
    out = strToBinStr(des.encrypt(binStrToStr(shiftreg)))
    cipherblock = int(out[:s], 2) ^ int(plaintext[i*s:(i+1)*s], 2)
    ciphertext += binStrToStr(cipherblock)
    shiftreg = shiftreg[s:64] + cipherblock
