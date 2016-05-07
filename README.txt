README.txt

Names:            Email:
Andrew Huynh      huynhah@csu.fullerton.edu
Alex Sanchez      asanchez1103@gmail.com
Eric Roe          ericroe@csu.fullerton.edu
Huy Le            hqle@csu.fullerton.edu
Sahar Ghanei      sghanei@csu.fullerton.edu
Joshua Womack     emailwomack@gmail.com

Programming Language: Python 3.4, tabs converted to spaces with 2 spaces per indentation

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

    python CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE> {<IV>}
    
    - IV is optional depending on the cipher
    
The following execution code was used before sending in the tar:
  DES Cipher:
    python CipherDriver.py VIG security ENC plainInput.txt encOutput.txt
    python CipherDriver.py VIG security DEC encOutput.txt encOutput.txt
  
  RSA Cipher:
    python CipherDriver.py RSA pubkey.pem ENC in.txt ciphered.txt
    python CipherDriver.py RSA privkey.pem DEC ciphered.txt deciphered.txt
  
  DES CFB/CBC:
    python CipherDriver.py DESCBC 0123456789abcdef ENC in.txt descbcEnciphered.txt abcdef12
    python CipherDriver.py DESCBC 0123456789abcdef DEC descbcEnciphered.txt descbcDeciphered.txt abcdef12
  
  RSA CFB/CBC:
    - todo

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

