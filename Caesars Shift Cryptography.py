#ASCII examples

#print (ord('A'))

#print (ord('a'))

#print (chr(97))


def encrypt(plaintext, key):
    ciphertext = ""

    for char in plaintext: #for loop
        num_char = ord(char) #ASCII
        num_ct = num_char + key #updating
        ciphertext += chr(num_ct)

    return ciphertext

#Modified:

inputtxt = input("Enter text you want to encrypt: ")

shift = input("Enter charcter shift: ")

encryptedtxt = (encrypt(inputtxt, int(shift)))

print("Encrypted text:", encryptedtxt)


### Authors personal note does not have anything to do with program
#Original:
#print(encrypt("Hello zebra", 3))
