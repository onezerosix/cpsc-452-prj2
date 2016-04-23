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
  AESCipher.py The Row Transposition Cipher implementation class
  
Extra Files:
  plainInput.txt            Example text input file

Makefile:
No makefile is necessary, just run the command in the terminal with all of the files in the folder.

Assumptions:
As specified in class, all input files contain only lowercase letters and assume no punctuation or spaces.

How to execute the program in the terminal:

    python3.4 CipherDriver.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>
    
The following execution code was used before sending in the tar:
  Vigenere Cipher:
    python3.4 CipherDriver.py VIG security ENC plainInput.txt encOutput.txt
    python3.4 CipherDriver.py VIG security DEC encOutput.txt encOutput.txt
  
  Caesar Cipher:
    python3.4 CipherDriver.py CES 3 ENC plainInput.txt encOutput.txt
    python3.4 CipherDriver.py CES 3 DEC encOutput.txt decOutput.txt
  
  Railfence Cipher:
    python3.4 CipherDriver.py RFC 3 ENC plainInput.txt encOutput.txt
    python3.4 CipherDriver.py RFC 3 DEC encOutput.txt decoutput.txt
  
  Playfair Cipher:
    python3.4 CipherDriver.py PLF security ENC plainInput.txt encOutput.txt
    python3.4 CipherDriver.py PLF security DEC encOutput.txt decOutput.txt
  
  Row Transposition Cipher:
    python3.4 CipherDriver.py RTS 4213 ENC plainInput.txt encOutput.txt
    python3.4 CipherDriver.py RTS 4213 DEC encOutput.txt decOutput.txt

• CIPHER NAME: Is the name of the cipher. Valid names are:
– PLF: Playfair
– RTS: Row Transposition
– RFC: Railfence
– VIG: Vigenre
– CES: Caesar

• KEY: the encryption key to use.
• ENC/DEC: whether to encrypt or decrypt, respectively.
• INPUT FILE: the file from which to read the input.
• OUTPUT FILE: the file to which the output shall be written.
