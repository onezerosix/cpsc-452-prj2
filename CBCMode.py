'''
  IV is going to be an 8 character string
  example of binary string: '100111010101010' (any length)
  example of string: 'k12lk~!^&HDF(*lkj*DSF(9.,'
  
  example runs
  python CipherDriver.py DESCBC 1234567890abcdef ENC long.txt out.txt 01234567
  python CipherDriver.py DESCBC 1234567890abcdef DEC out.txt out2.txt 01234567
  python CipherDriver.py RSACBC pubkey.pem ENC long.txt out.txt 01234567
  python CipherDriver.py RSACBC privkey.pem DEC out.txt out2.txt 01234567
'''
from DESCipher import DESCipher
from RSACipher import RSACipher

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

def encryptCBC(cipher, plaintext, IV, n): # IV will be n bytes hence plaintext and ciphertext blocks will be n bytes
  ciphertext = ""			                                    # ciphertext will hold the encrypted plaintext
  cipher_block = IV                                       # initialize variable with IV in bits
  
  if len(plaintext)%n != 0: # pad plaintext if needed
    plaintext += '0' * (n - (len(plaintext)%n)) # pad with as many 0's as it requires for the last block to become 8 bytes
    
  plaintext_in_blocks = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]  # Loop through plaintext and split in blocks of 8 bytes (64 bits)
  
  for block in plaintext_in_blocks: # Loop through all the blocks (8 bytes each) in the plaintext
    plaintext_in_bits = strToBinStr(block) # Convert the current block from string to binary for xor
    cipher_in_bits = strToBinStr(cipher_block) # Convert the previous cipher block from string to binary for xor
    current_block_xor = bin(int(plaintext_in_bits, 2) ^ int(cipher_in_bits, 2))[2:] # xor the plaintext and previous cipher block
    current_block_xor = ("0" * (n*8 - len(current_block_xor))) + current_block_xor # prepend missing 0's if needed 
    current_block_str = binStrToStr(current_block_xor) # Convert the xored result from binary to string
    cipher_block = cipher.encrypt(current_block_str) # The current block has been processed and is encrypted here
    ciphertext += cipher_block # Add this block to the ciphertext
  return ciphertext

def decryptCBC(cipher, ciphertext, IV, n): # IV will be n bytes hence plaintext and ciphertext blocks will be n bytes
  plaintext = ""			                                   # plaintext will hold the decrypted ciphertext
  prev_cipher_block = IV                                 # initialize variable with IV in bits
  
  # if ciphertext isn't divisible by n, n is wrong
  if len(ciphertext)%n != 0:
    print "WARNING: ciphertext doesn't fit correctly into blocks, this may cause errors."
    
  ciphertext_in_blocks = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]  # Loop through ciphertext and split in blocks of n bytes
  
  for block in ciphertext_in_blocks: # Loop through all the blocks (8 bytes each) in the ciphertext
    decrypted_block = cipher.decrypt(block) # Decrypt the current block
    if len(block) != len(decrypted_block):
      print "WARNING: size of block after decryption has changed."
    decrypted_in_bits = strToBinStr(decrypted_block) # Convert the current block from string to binary
    prev_cipher_bits = strToBinStr(prev_cipher_block) # Convert the previous cipher block from string to binary
    current_block_xor = bin(int(decrypted_in_bits, 2) ^ int(prev_cipher_bits, 2))[2:] # xor the decrypted ciphertext with the previous ciphertext
    current_block_xor = ("0" * (n*8 - len(current_block_xor))) + current_block_xor # prepend missing 0's if needed 
    plain_block = binStrToStr(current_block_xor) # Convert the xored result from binary to string
    prev_cipher_block = block # Set the previous cipherblock to the current ciphertext block
    plaintext += plain_block # Add this block to the plaintext
  return plaintext
