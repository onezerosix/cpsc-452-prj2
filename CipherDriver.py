"""
CPSC 452
Assignment 2
Cipher Driver

Python 2.7

Modified 4/23/16: Eric Roe

Updated to include DES and RSA cipher options.
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
  # python CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUTFILE>
  # python CipherDriver.py DESCBC <KEY> <ENC/DEC> <INPUTFILE> <OUTPUTFILE> <IV> # similar usage for DESCFB/RSACBC/RSACFB

  # check number of parameters
  if len(sys.argv) != 6 and len(sys.argv) != 7 and len(sys.argv) != 8:
    badUser("ERROR: incorrect number of parameters provided\ncheck README")
  
  cipherName = sys.argv[1]                                  # <CIPHER NAME>
  key = sys.argv[2]                                         # <KEY>
  mode = sys.argv[3]                                        # <ENC/DEC>
  inputFile = sys.argv[4]                                   # <INPUTFILE>
  outputFile = sys.argv[5]                                  # <OUTPUTFILE>

  # for CBC and CFB modes
  if cipherName in {"DESCBC", "RSACBC"}: # set of CBC mode ciphers
    if len(sys.argv) != 7:
      badUser("ERROR: need to provide IV parameter for CBC/CFB\ncheck README")
    else:
      IV = sys.argv[6]
  elif cipherName in {"DESCFB", "RSACFB"}: # set of CFB mode ciphers
    # TODO: implement later
    IV = sys.argv[6]
    s = int(sys.argv[7])
  elif len(sys.argv) != 6:
    badUser("ERROR: incorrect number of parameters for ECB\ncheck README")

  toConvert = readFile(inputFile)                           # attempt to read file
  
  if cipherName == "DES":                                   # <CIPHER NAME> = DES --> DES Cipher
    cipher = DESCipher()                                       # Create an instance of the class
    if cipher.setKey(key) == False:                            # Attempt to set the key
      badUser("Invalid key for DES Cipher. Key must be 16 hexidecimal characters (0-9, a-f)!")

  elif cipherName == "RSA":
    cipher = RSACipher()                                       # <CIPHER NAME> = RSA --> RSA Cipher
    if cipher.setKey(key) == False:                            # Attempt to set the key
      #TODO: know key reqs
      badUser("Invalid key for RSA Cipher. Key can only be ?")

  elif cipherName == "DESCFB":
    cipher = DESCipher()                                       # Create an instance of the class
    if cipher.setKey(key) == False:                            # Attempt to set the key
      badUser("Invalid key for DES Cipher. Key must be 16 hexidecimal characters (0-9, a-f)!")

  elif cipherName == "RSACFB":
    cipher = RSACipher()                                       # Create an instance of the class
    if cipher.setKey(key) == False:                            # Attempt to set the key
      #TODO: know key reqs
      badUser("Invalid key for RSA Cipher. Key can only be ?")

  else:                                                     # Invalid Cipher
    badUser("Invalid <CIPHER NAME>, please use the following names:\
            \n- DES: Data Encryption Standard\
            \n- RSA: Row Transposition")

  if mode == "ENC":
    print("ENC: Encryption mode selected. Encrypting...")
    if cipherName in {"DESCBC", "RSACBC"}:
      #TODO: implement
      badUser("CBC not implemented yet")
    elif cipherName in {"DESCFB", "RSACFB"}:
      converted = encryptCFB(cipher, toConvert, IV, s)
    else:
      converted = cipher.encrypt(toConvert)                     # Encrypt and receive the ciphered text
    print("The ciphered text is: {}".format(converted))
  elif mode == "DEC":
    print("DEC: Decryption mode selected. Decrypting...")
    if cipherName in {"DESCBC", "RSACBC"}:
      #TODO: implement
      badUser("CBC not implemented yet")
    elif cipherName in {"DESCFB", "RSACFB"}:
      converted = decryptCFB(cipher, toConvert, IV, s)
    else:
      converted = cipher.decrypt(toConvert)                   # Decrypt and receive the deciphered text
    print("The deciphered text is: {}".format(converted))
  else:
    badUser("Error, please specify <ENC/DEC>")

  writeFile(outputFile, converted)                            # print converted text
      
if __name__ == '__main__':
  main( )
