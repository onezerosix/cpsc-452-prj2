def strToBinStr(myS): # translate a string to a binary string
  myL = []
  for i in range(len(myS)):
    x = bin(ord(myS[i]))[2:] # i-th char in myS to int to binary & strip '0b' (gets a binary string)
    x = ('0' * (8 - len(x))) + x # prepend missing 0s if needed
    myL.append(x)
  return ''.join(myL)
  
def binStrToStr(myB): # undo strToBinStr - translate binary string to regular string
  myS = ''
  for i in range(0, len(myB), 8): # translate 8 bits at a time
    myS += chr(int(myB[i:i+8], 2))
  return myS

# if ciphertext isn't divisible by correct size, strToBinStr put extra padding or s is wrong
# the extra padding would be on the last byte so attempt to fix it
def trimLastByte(ciphertext, size):
  if len(ciphertext)%size != 0:
    x = len(ciphertext) % size # amount of extra leading padding of last byte
    zeros = 8 - len(ciphertext[-8:].lstrip('0')) # amount of leading zeros
    numKeep = zeros - x # amount of zeros to keep
    if numKeep < 0:
      print "WARNING: size may be incorrect"
    else:
      temp = ciphertext[-8:].lstrip('0') # remove leading padding of last byte
      temp = ('0' * numKeep) + temp # last byte with correct num bytes
      ciphertext = ciphertext[:-8] + temp # update ciphertext
      if len(ciphertext)%size != 0:
        print "WARNING: attempted to fit ciphertext to correct size but failed"
  return ciphertext
