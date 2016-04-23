"""
CPSC 452
Assignment 2
Cipher Driver

Python 2.7

Modified 4/23/16: Eric Roe

Updated to include DES and RSA cipher options.
"""



# TODO: Add CBC and CFB modes




import sys
from CipherInterface import CipherInterface
from DESCipher import DESCipher
from RSACipher import RSACipher

# Attempt to read the content of the specified filename
def readFile(fileName):                                     
  with open(fileName, 'r') as ifh:                          # Open the file with read permissions
    text = ifh.read()
  return text
  
# Attempt to write the content to the specified filename
def writeFile(fileName, content):
  with open(fileName, 'w') as ofh:                          # Open the file with write permissions
    ofh.write(content)                                      # Write the contents to the file

def main ( ):
  # python CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUTFILE>
  cipherName = sys.argv[1]                                  # <CIPHER NAME>
  key = sys.argv[2]                                         # <KEY>
  mode = sys.argv[3]                                        # <ENC/DEC>
  inputFile = sys.argv[4]                                   # <INPUTFILE>
  outputFile = sys.argv[5]                                  # <OUTPUTFILE>
  
  if cipherName == "DES":                                   # <CIPHER NAME> = DES --> DES Cipher
    des = DESCipher()                                       # Create an instance of the class
    if des.setKey(key) == False:                            # Attempt to set the key
      print("Invalid key for DES Cipher. Key must be 16 hexidecimal characters (0-9, a-f)!")
      sys.exit()                                            # Exit Program
    toConvert = readFile(inputFile)                         # Read the file and make sure it's lowercase
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = des.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFile
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = des.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  elif cipherName == "RSA":
    rsa = RSACipher()                                       # <CIPHER NAME> = RSA --> RSA Cipher
    if rsa.setKey(key) == False:                            # Attempt to set the key
      #TODO: know key reqs
      print("Invalid key for RSA Cipher. Key can only be ?")
      sys.exit()                                            # Exit program
    toConvert = readFile(inputFile)                         # Read the file and make sure it's lowercase
    if mode == "ENC":
      print("ENC: Encryption mode selected. Encrypting...")
      ciphered = rsa.encrypt(toConvert)                     # Encrypt and receive the ciphered text
      print("The ciphered text is: {}".format(ciphered))
      writeFile(outputFile, ciphered)                       # Write the ciphered text to the specified outputFIle
    elif mode == "DEC":
      print("DEC: Decryption mode selected. Decrypting...")
      deciphered = rsa.decrypt(toConvert)                   # Decrypt and receive the deciphered text
      print("The deciphered text is: {}".format(deciphered))
      writeFile(outputFile, deciphered)                     # Write the deciphered text to the specified outputFile
    else:
      print("Error, please specify <ENC/DEC>")
  else:                                                     # Invalid Cipher
    print("Invalid <CIPHER NAME>, please use the following names:")
    print("- DES: Data Encryption Standard")
    print("- RSA: Row Transposition")
      
if __name__ == '__main__':
  main( )
