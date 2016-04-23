"""
Railfence
CPSC 452
Assignment 1
Cipher Driver
"""

import sys
from CipherInterface import CipherInterface
from VigenereCipher import Vigenere
from CaesarCipher import Caesar
from RailfenceCipher import Railfence
from PlayfairCipher import Playfair
from RowTranspositionCipher import RowTransposition

# Attempt to read the content of the specified filename
def readFile(fileName):
  contents = []                                             # Empty list for file contents
  with open(fileName, 'r') as ifh:                          # Open the file with read permissions
    for line in ifh:                                        # For each line in the file
      contents.append(line)                                 # Add each line to the list
    contents = ''.join(contents)                            # Combines the list to a string
  contents = contents.replace('\n', '').replace(' ','').lower()
  return contents
  
# Attempt to write the content to the specified filename
def writeFile(fileName, content):
  with open(fileName, 'w') as ofh:                          # Open the file with write permissions
    print(content, file = ofh, end = '')                    # Write the contents to the file

def main ( ):
  # python3.4 CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUTFILE>
  cipherName = sys.argv[1]                                  # <CIPHER NAME>
  key = sys.argv[2]                                         # <KEY>
  mode = sys.argv[3]                                        # <ENC/DEC>
  inputFile = sys.argv[4]                                   # <INPUTFILE>
  outputFile = sys.argv[5]                                  # <OUTPUTFILE>
  
  if cipherName == "VIG":                                   # <CIPHER NAME> = VIG --> Vigenere Cipher
    vig = Vigenere()                                        # Create an instance of the class
    if vig.setKey(key) == False:                            # Attempt to set the key
      print("Invalid key for Vigenere Cipher. Key can only contain alphabetical characters!")
      sys.exit()                                            # Exit Program
    toConvert = readFile(inputFile)                         # Read the file and make sure it's lowercase
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = vig.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFile
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = vig.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  elif cipherName == "CES":
    ces = Caesar()                                          # <CIPHER NAME> = CES --> Caesar Cipher
    if ces.setKey(key) == False:                            # Attempt to set the key
      print("Invalid key for Caesar Cipher. Key can only be numbers from 1-26")
      sys.exit()                                            # Exit program
    toConvert = readFile(inputFile)                         # Read the file and make sure it's lowercase
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = ces.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFIle
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = ces.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  elif cipherName == "RFC":
    rfc = Railfence()                                       # <CIPHER NAME> = RFC --> Railfence Cipher
    if rfc.setKey(key) == False:                            # Attempt to set the key
      print("Invalid key for Railfence Cipher. Key must consist of digits from 0-9")
      sys.exit()                                            # Exit program
    toConvert = readFile(inputFile)                         # Read the file and make sure it's lowercase
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = rfc.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFIle
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = rfc.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  elif cipherName == "PLF":
    plf = Playfair()
    if plf.setKey(key) == False:
      print("Invalid key for Playfair Cipher. Key can only contain alphabetical characters!")
      sys.exit()
    toConvert = readFile(inputFile)
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = plf.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFile
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = plf.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  elif cipherName == "RTS":
    rts = RowTransposition()                                # <CIPHER NAME> = CES --> Row Transposition Cipher
    if rts.setKey(key) == False:                            # Attempt to set the key
      print("Invalid key for Row Transposition Cipher. Key can only be a number >= 1.")
      sys.exit()                                            # Exit program
    toConvert = readFile(inputFile)                         # Read the file and make sure it's lowercase
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = rts.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFIle
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = rts.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  else:                                                     # Invalid Cipher
    print("Invalid <CIPHER NAME>, please use the following names:")
    print("- PLF: Playfair")
    print("- RTS: Row Transposition")
    print("- RFC: Railfence")
    print("- VIG: Vigenere")
    print("- CES: Caesar")
      
if __name__ == '__main__':
  main( )
