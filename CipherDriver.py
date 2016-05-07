"""
CPSC 452
Assignment 2
Cipher Driver

Python 2.7
"""

import sys
from CipherInterface import CipherInterface
from DESCipher import DESCipher
from RSACipher import RSACipher
from CFBMode import *

# Attempt to read the content of the specified filename
def readFile(fileName):     
  try:                                
    with open(fileName, 'r') as ifh:                          # Open the file with read permissions
      text = ifh.read()
    return text
  except IOError:
    badUser("ERROR: could not read to " + fileName)
  
  
# Attempt to write the content to the specified filename
def writeFile(fileName, content):
  try:
    with open(fileName, 'w') as ofh:                          # Open the file with write permissions
      ofh.write(content)                                      # Write the contents to the file
  except IOError:
    badUser("ERROR: could not write to  " + fileName)

# program used incorrectly by user
def badUser(msg):
  print(msg)
  sys.exit(-1)

def main ( ):
  # check number of parameters
  if len(sys.argv) != 6 and len(sys.argv) != 7 and len(sys.argv) != 8:
    badUser("ERROR: incorrect number of parameters provided\ncheck README")

  cipherName = sys.argv[1]                                  # <CIPHER NAME>
  key = sys.argv[2]                                         # <KEY>
  mode = sys.argv[3]                                        # <ENC/DEC>
  inputFile = sys.argv[4]                                   # <INPUTFILE>
  outputFile = sys.argv[5]                                  # <OUTPUTFILE>

  # deeper check of number of parameters
  if cipherName in {"DESCBC", "RSACBC"}: # set of CBC mode ciphers
    if len(sys.argv) != 7:
      badUser("ERROR: incorrect number of parameters for CBC\ncheck README")
    else:
      IV = sys.argv[6]
  elif cipherName in {"DESCFB", "RSACFB"}: # set of CFB mode ciphers
    if len(sys.argv) != 8:
      badUser("ERROR: incorrect number of parameters for CFB\ncheck README")
    else:
      IV = sys.argv[6]
      try: # ensure s is an int
        s = int(sys.argv[7])
      except ValueError:
        badUser("ERROR: s argument provided couldn't translate to a 10-base int\ncheck README")      
  elif len(sys.argv) != 6:
    badUser("ERROR: incorrect number of parameters for ECB\ncheck README")

  toConvert = readFile(inputFile)                           # attempt to read file
  
  if cipherName in {"DES", "DESCBC", "DESCFB"}:
    cipher = DESCipher()                                       # Create an instance of the class
    if cipher.setKey(key) == False:                            # Attempt to set the key
      badUser("Invalid key for DES Cipher. Key must be 16 hexidecimal characters (0-9, a-f)!")

  elif cipherName in {"RSA", "RSACBC", "RSACFB"}:
    cipher = RSACipher()
    if cipher.setKey(key) == False:                            # Attempt to set the key
      badUser("Setting RSA key failed\ncheck README")

  else:                                                     # Invalid Cipher
    badUser("Invalid <CIPHER NAME>\ncheck README")

  if mode == "ENC":
    print("ENC: Encryption mode selected. Encrypting...")
    if cipherName in {"DESCBC", "RSACBC"}:
      #TODO: implement CBC
      badUser("CBC not implemented yet")
    elif cipherName in {"DESCFB", "RSACFB"}:
      converted = encryptCFB(cipher, toConvert, IV, s)
    else:
      converted = cipher.encrypt(toConvert)                     # Encrypt and receive the ciphered text
    print("The ciphered text is: {}".format(converted))

  elif mode == "DEC":
    print("DEC: Decryption mode selected. Decrypting...")
    if cipherName in {"DESCBC", "RSACBC"}:
      #TODO: implement CBC
      badUser("CBC not implemented yet")
    elif cipherName in {"DESCFB", "RSACFB"}:
      converted = decryptCFB(cipher, toConvert, IV, s)
    else:
      converted = cipher.decrypt(toConvert)                   # Decrypt and receive the deciphered text
    print("The deciphered text is: {}".format(converted))
  else:
    badUser("ERROR: please specify <ENC/DEC>")

  writeFile(outputFile, converted)                            # print converted text
      
if __name__ == '__main__':
  main( )
