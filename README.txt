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
  DES-CFB-Cipher.py         The DES Cipher implementation class with CFB mode
  DES-CBC-Cipher.py         The DES Cipher implementation class with CBC mode
  RSA-CFB-Cipher.py         The RSA Cipher implementation class with CFB mode
  RSA-CBC-Cipher.py         The RSA Cipher implementation class with CBC mode
  
Extra Files:
  in.txt            Example text input file
  pubkey.pem        Test key used for encryption in RSA
  privkey.pem       Test key used for decryption in RSA

Makefile:
No makefile is necessary, just run the command in the terminal with all of the files in the folder.

Assumptions:
As specified in class, all input files contain only lowercase letters and assume no punctuation or spaces.
Pycrypto was used in both implementations, install using:
  $pip install pycrypto

How to execute the program in the terminal:

    python3.4 CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE> {<IV>}
    
The following execution code was used before sending in the tar:
  DES Cipher:
    python3.4 CipherDriver.py VIG security ENC plainInput.txt encOutput.txt
    python3.4 CipherDriver.py VIG security DEC encOutput.txt encOutput.txt
  
  RSA Cipher:
    python CipherDriver.py RSA pubkey.pem ENC in.txt ciphered.txt
    python CipherDriver.py RSA privkey.pem DEC ciphered.txt deciphered.txt
  
  DES CFB/CBC:
    - todo
  
  RSA CFB/CBC:
    - todo

• CIPHER NAME: Is the name of the cipher. Valid names are:
- DES: Data encryption standard
- DES-CFB: DES using CFB mode
- DES-CBC: DES using CBC mode
- RSA: RSA algorithm
- RSA-CFB: RSA using CFB mode
- RSA-CBC: RSA using CBC mode

• KEY: the encryption key to use, for RSA it is the name of the .pem key file
• ENC/DEC: whether to encrypt or decrypt, respectively.
• INPUT FILE: the file from which to read the input.
• OUTPUT FILE: the file to which the output shall be written.
