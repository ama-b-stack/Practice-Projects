# the caesar cipher is one of the simplest encryption methods
# that uses a key to shift each given letter by a certain number
# of positions to create a secret code

# import string module #
import string

# to use string.ascii_lowercase constant #
alphabet = string.ascii_lowercase

# intro and accept key and secret #
print("This is my attempt at creating a Caesar Cipher.\n")

secret = input("Please enter a secret message: ").strip()                    # strip python method removes leading and trailing space #
print()
key = int(input("Enter the key: "))

# define the *encrypt* function, which finds the numeric position
# of each given letter in the alphabet, adds the key from
# this numeric position given 26 letters, and returns that new
# position as a letter
def encrypt():

    global secret, key                                                      # access external vars secret and key #

    encrypt = ""

    for e in secret:                                                        # for loop that iterates through each letter of the input string in the alphabet and adds the key to the position #

        if e in alphabet:
            position = alphabet.find(e)                                     # find method finds occurence of input letter in our alphabet variable #
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            encrypt += new_character

    print("Your encrypted message: " + encrypt)

# define the *decrypt* function, which finds the numeric position
# of each given letter in the alphabet, subtracts the key from
# this numeric position given 26 letters, and returns that new
# position as a letter

def decrypt():

    global secret, key                                                     # access external vars secret and key #

    decrypt = ""

    for d in secret:

        if d in alphabet:
            position = alphabet.find(d)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypt += new_character
        else:
            decrypt += d

    print("Your decrypted message: " + decrypt)

# user chooses whether to encrypt or decrypt using given key,
# appropriate function is called.
print("Would you like this message encrypted or decrypted?\n")
selection = int(input("Enter 1 for encryption and 2 for decryption: "))

if selection == 1:
    encrypt()
elif selection == 2:
    decrypt()
