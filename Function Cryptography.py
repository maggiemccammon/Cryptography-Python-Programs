#Function 

def xor(char1, char2):
    ascii_val1 = ord(char1)
    ascii_val2 = ord(char2)

#xor of ascii
    conversion = ascii_val1 ^ ascii_val2

    return conversion

char1 = input("Enter an uppercase letter A-Z: ")
char2 = input("Enter an uppercase letter A-Z: ") 

conversion = xor(char1, char2)

print(f'xor("{char1}", "{char2}") = {conversion}')



    
