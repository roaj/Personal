#My first python program - Caesar Cypher ROT13

def encryptCaesar(message):
    ciphertext = ""

    for character in message:
        print(character)
        if character == 'a':
            ciphertext = ciphertext + 'n'
        elif character == 'b':
            ciphertext = ciphertext + 'o'
        elif character == 'c':
            ciphertext = ciphertext + 'p'
        elif character == 'd':
            ciphertext = ciphertext + 'q'
        elif character == 'e':
            ciphertext = ciphertext + 'r'
        elif character == 'f':
            ciphertext = ciphertext + 's'
        elif character == 'g':
            ciphertext = ciphertext + 't'
        elif character == 'h':
            ciphertext = ciphertext + 'u'
        elif character == 'i':
            ciphertext = ciphertext + 'v'
        elif character == 'j':
            ciphertext = ciphertext + 'w'
        elif character == 'k':
            ciphertext = ciphertext + 'x'
        elif character == 'l':
            ciphertext = ciphertext + 'y'
        elif character == 'm':
            ciphertext = ciphertext + 'z'
        elif character == 'n':
            ciphertext = ciphertext + 'a'
        elif character == 'o':
            ciphertext = ciphertext + 'b'
        elif character == 'p':
            ciphertext = ciphertext + 'c'
        elif character == 'q':
            ciphertext = ciphertext + 'd'
        elif character == 'r':
            ciphertext = ciphertext + 'e'
        elif character == 's':
            ciphertext = ciphertext + 'f'
        elif character == 't':
            ciphertext = ciphertext + 'g'
        elif character == 'u':
            ciphertext = ciphertext + 'h'
        elif character == 'v':
            ciphertext = ciphertext + 'i'
        elif character == 'w':
            ciphertext = ciphertext + 'j'
        elif character == 'x':
            ciphertext = ciphertext + 'k'
        elif character == 'y':
            ciphertext = ciphertext + 'l'
        elif character == 'z':
            ciphertext = ciphertext + 'm'
        else:
            #if character is not an alphabet letter, the character is appended to the ciphertext
            ciphertext = ciphertext + character
    return ciphertext    


#main file (you can do this in a separate file and import your file where you define your functions
plaintext = input("\nPlease enter a word to be encrypted:")
print("plaintext is: " + plaintext + '\n')

#convert to lower case
plaintext = plaintext.lower()

#call the function to encryp
ciphertext = encryptCaesar(plaintext)
print("ciphertext is: ", ciphertext)
