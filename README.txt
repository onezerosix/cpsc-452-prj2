README.txt

Names:            Email:
Andrew Huynh      huynhah@csu.fullerton.edu
Alex Sanchez      asanchez1103@gmail.com
Eric Roe          ericroe@csu.fullerton.edu
Huy Le            hqle@csu.fullerton.edu
Sahar Ghanei      sghanei@csu.fullerton.edu
Joshua Womack     emailwomack@gmail.com

Programming Language: Python, tabs converted to spaces with 2 spaces per indentation

Filename:               Description:
  README.txt                The current file with instructions and other information
  __init__.py               Required to make Python treat the directories as containing packages
  CipherDriver.py           The main program that will be called
  CipherInterface.py        The base class used in the cipher classes
  DESCipher.py              The DES Cipher implementation class
  RSACipher.py              The RSA Cipher implementation class
  DESCFBCipher.py           The DES Cipher implementation class with CFB mode
  DESCBCCipher.py           The DES Cipher implementation class with CBC mode
  RSACFBCipher.py           The RSA Cipher implementation class with CFB mode
  RSACBCCipher.py           The RSA Cipher implementation class with CBC mode
  
Extra Files:
  in.txt            Example text input file
  long.txt          Long example text input file
  pubkey.pem        Test key used for encryption in RSA
  privkey.pem       Test key used for decryption in RSA

Makefile:
No makefile is necessary, just run the command in the terminal with all of the files in the folder.

Assumptions:
- The file is in a readable format and encoded using UTF-8.
- After an encrypted file is decrypted, the user will manually remove the padding if desired.

Pycrypto was used in both implementations, install using:
  $pip install pycrypto

How to execute the program in the terminal:

    python CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE> {<IV>} {<SBits>}
    
    - IV is necessary when using CBC or CFB modes
    - SBits is necessary when using CFB mode. 
    
Extra Credit:
Our group implemented the extra credit for the DES Cipher. 
We also implemented CBC and CFB modes for the RSA Cipher for additional extra credit 
as discussed after class on 5/2/26. 


The following executions were tested where plaintext.txt was replaced with either in.txt or long.txt:

  DES Cipher (@params - CIPHER NAME, KEY, ENC/DEC, INPUTFILE, OUTPUTFILE):
    python CipherDriver.py DES 1234567890abcdef ENC plaintext.txt DESenc.txt
    python CipherDriver.py DES 1234567890abcdef DEC DESenc.txt DESdec.txt

  RSA Cipher (@params - CIPHER NAME, PUBLICKEY/PRIVATEKEY, ENC/DEC, INPUTFILE, OUTPUTFILE):
    python CipherDriver.py RSA pubkey.pem ENC plaintext.txt RSAenc.txt
    python CipherDriver.py RSA privkey.pem DEC RSAenc.txt RSAdec.txt
  
  DES Cipher - CBC mode (@params - CIPHER NAME, KEY, ENC/DEC, INPUTFILE, OUTPUTFILE, IV):
    python CipherDriver.py DESCBC 0123456789abcdef ENC plaintext.txt DESCBCenc.txt abcdef12
    python CipherDriver.py DESCBC 0123456789abcdef DEC DESCBCenc.txt DESCBCdec.txt abcdef12

  DES Cipher - CFB mode (@params - CIPHER NAME, KEY, ENC/DEC, INPUTFILE , OUTPUTFILE , IV, sBitSelection):
    python CipherDriver.py DESCFB 1234567890abcdef ENC plaintext.txt DESCFBenc.txt 01234567 57
    python CipherDriver.py DESCFB 1234567890abcdef DEC DESCFBenc.txt DESCFBdec.txt 01234567 57

  RSA Cipher - CBC mode (@params - CIPHER NAME, PUBLICKEY/PRIVATEKEY, ENC/DEC, INPUTFILE, OUTPUTFILE, IV):
    python CipherDriver.py RSACBC pubkey.pem ENC plaintext.txt RSACBCenc.txt 01234567
    python CipherDriver.py RSACBC privkey.pem DEC RSACBCenc.txt RSACBCdec.txt 01234567
  
  RSA Cipher- CFB mode (@params - CIPHER NAME, PUBLICKEY/PRIVATEKEY, ENC/DEC, INPUTFILE , OUTPUTFILE , IV, sBitSelection):
    python CipherDriver.py RSACFB pubkey.pem ENC plaintext.txt RSACFBenc.txt 01234567 30
    python CipherDriver.py RSACFB privkey.pem DEC RSACFBenc.txt RSACFBdec.txt 01234567 30

• CIPHER NAME: Is the name of the cipher. Valid names are:
- DES: Data encryption standard
- DESCFB: DES using CFB mode
- DESCBC: DES using CBC mode
- RSA: RSA algorithm
- RSACFB: RSA using CFB mode
- RSACBC: RSA using CBC mode

• KEY: the encryption key to use, for RSA it is the name of the .pem key file
• ENC/DEC: whether to encrypt or decrypt, respectively.
• INPUT FILE: the file from which to read the input.
• OUTPUT FILE: the file to which the output shall be written.

