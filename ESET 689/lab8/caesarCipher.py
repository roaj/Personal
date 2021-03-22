#My first python program - Caesar Cypher

def encryptCaesar(message):
    ciphertext = ""

    for character in message:
        print(character)
        if character == 'a':
            ciphertext = ciphertext + 'd'
        elif character == 'b':
            ciphertext = ciphertext + 'e'
        elif character == 'c':
            ciphertext = ciphertext + 'f'
        elif character == 'd':
            ciphertext = ciphertext + 'g'
        elif character == 'e':
            ciphertext = ciphertext + 'h'
        elif character == 'f':
            ciphertext = ciphertext + 'i'
        elif character == 'g':
            ciphertext = ciphertext + 'j'
        elif character == 'h':
            ciphertext = ciphertext + 'k'
        elif character == 'i':
            ciphertext = ciphertext + 'l'
        elif character == 'j':
            ciphertext = ciphertext + 'm'
        elif character == 'k':
            ciphertext = ciphertext + 'm'
        elif character == 'l':
            ciphertext = ciphertext + 'o'
        elif character == 'm':
            ciphertext = ciphertext + 'p'
        elif character == 'n':
            ciphertext = ciphertext + 'q'
        elif character == 'o':
            ciphertext = ciphertext + 'r'
        elif character == 'p':
            ciphertext = ciphertext + 's'
        elif character == 'q':
            ciphertext = ciphertext + 't'
        elif character == 'r':
            ciphertext = ciphertext + 'u'
        elif character == 's':
            ciphertext = ciphertext + 'v'
        elif character == 't':
            ciphertext = ciphertext + 'w'
        elif character == 'u':
            ciphertext = ciphertext + 'x'
        elif character == 'v':
            ciphertext = ciphertext + 'y'
        elif character == 'w':
            ciphertext = ciphertext + 'z'
        elif character == 'x':
            ciphertext = ciphertext + 'a'
        elif character == 'y':
            ciphertext = ciphertext + 'b'
        elif character == 'z':
            ciphertext = ciphertext + 'c'
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


    


     

