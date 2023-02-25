import string
# the code is designed to allow the user to Choose a cipher (Caesar or Vigenere or playfair or affine) Additionally,
# it is possible that the user is prompted to input the key for the selected cipher also to select the encryption mode
# (encryption or decryption)



##encrypt playfair

# Function to convert the string to lowercase
def toLowerCase(text):
    return text.lower()


# Function to remove all spaces in a string
def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText


# Function to group 2 elements of a string
# as a list element
def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph


# Function to fill a letter in a string elementd
# If 2 letters in the same string matches
def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Function to generate the 5x5 key square matrix
def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == element):
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c + 1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c + 1]

    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r + 1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r + 1][e2c]

    return char1, char2


def encrypt_playfair(text, key):
    text = toLowerCase(text)
    text = removeSpaces(text)
    text = Diagraph(text)
    text = FillerLetter(text)
    key = toLowerCase(key)
    key = removeSpaces(key)
    key = FillerLetter(key)
    key_matrix = generateKeyTable(key, list1)

    cipher_text = ""
    for i in text:
        e1 = i[0]
        e2 = i[1]
        e1_coord = search(key_matrix, e1)
        e2_coord = search(key_matrix, e2)
        if e1_coord[0] == e2_coord[0]:
            char1, char2 = encrypt_RowRule(key_matrix, e1_coord[0], e1_coord[1], e2_coord[0], e2_coord[1])
        elif e1_coord[1] == e2_coord[1]:
            char1, char2 = encrypt_ColumnRule(key_matrix, e1_coord[0], e1_coord[1], e2_coord[0], e2_coord[1])
        else:
            char1 = key_matrix[e1_coord[0]][e2_coord[1]]
            char2 = key_matrix[e2_coord[0]][e1_coord[1]]
        cipher_text = cipher_text + char1 + char2

    return cipher_text

##caesar_encrypt
def caesar_encrypt(plaintext, shift):
    # Create a string of lowercase letters for the alphabet
    alphabet = string.ascii_lowercase
    # Initialize the empty ciphertext variable
    ciphertext = ""
    # Iterate through each character in the plaintext
    for char in plaintext:
        # Check if the character is a letter
        if char in alphabet:
            # Shift the letter by the specified amount
            shifted_index = (alphabet.index(char) + shift) % 26
            # Add the shifted letter to the ciphertext
            ciphertext += alphabet[shifted_index]
        else:
            # Add non-letter characters to the ciphertext as is
            ciphertext += char
    # Return the final ciphertext
    return ciphertext

##caesar_decrypt
def caesar_decrypt(ciphertext, shift):
    # Create a string of lowercase letters for the alphabet
    alphabet = string.ascii_lowercase
    # Initialize the empty plaintext variable
    plaintext = ""
    # Iterate through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is a letter
        if char in alphabet:
            # Shift the letter by the specified amount
            shifted_index = (alphabet.index(char) - shift) % 26
            # Add the shifted letter to the plaintext
            plaintext += alphabet[shifted_index]
        else:
            # Add non-letter characters to the plaintext as is
            plaintext += char
    # Return the final plaintext
    return plaintext

##vigenere_encrypt
def vigenere_encrypt(plaintext, key):
    # Create a string of lowercase letters for the alphabet
    alphabet = string.ascii_lowercase
    key = key.lower()
    # Initialize the empty ciphertext variable
    ciphertext = ""
    key_index = 0
    # Iterate through each character in the plaintext
    for char in plaintext:
        # Check if the character is a letter
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            shifted_index = (alphabet.index(char) + shift) % 26
            # Add the shifted letter to the ciphertext
            ciphertext += alphabet[shifted_index]
            key_index = (key_index + 1) % len(key)
        else:
            # Add non-letter characters to the ciphertext as is
            ciphertext += char
    # Return the final ciphertext
    return ciphertext

##vigenere_decrypt
def vigenere_decrypt(ciphertext, key):
    # Create a string of lowercase letters for the alphabet
    alphabet = string.ascii_lowercase
    key = key.lower()
    # Initialize the empty plaintext variable
    plaintext = ""
    key_index = 0
    # Iterate through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is a letter
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            shifted_index = (alphabet.index(char) - shift) % 26
            # Add the shifted letter to the plaintext
            plaintext += alphabet[shifted_index]
            key_index = (key_index + 1) % len(key)
        else:
            # Add non-letter characters to the plaintext as is
            plaintext += char
    # Return the final plaintext
    return plaintext

##encrypt_affine
def encrypt_affine(plaintext, key):
    a, b = key
    ciphertext = ""
    for i in plaintext:
        # Check if the character is an alphabet
        if i.isalpha():
            # Encryption formula for affine cipher
            c = (a * ord(i) + b) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += i
    return ciphertext

##decrypt_affine
def decrypt_affine(ciphertext, key):
    a, b = key
    plaintext = ""
    for i in ciphertext:
        # Check if the character is an alphabet
        if i.isalpha():
            # Decryption formula for affine cipher
            p = (26 + (ord(i) - b) * a) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += i
    return plaintext


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    cipher = input("Choose a cipher (Caesar or Vigenere or playfair or affine): ")
    mode = input("Choose mode (encrypt or decrypt): ")
    if cipher == "Caesar":
        shift = int(input("Shift: "))
        if mode == "encrypt":
            ciphertext = caesar_encrypt(plaintext, shift)
            print("Ciphertext: ", ciphertext)
        elif mode == "decrypt":
            ciphertext = caesar_decrypt(plaintext, shift)
            print("Original text: ", ciphertext)
        else:
            print("Invalid mode, please choose 'encrypt' or 'decrypt'.")
    elif cipher == "Vigenere":
        key = input("Enter the key text: ")
        if mode == "encrypt":
            ciphertext = vigenere_encrypt(plaintext, key)
            print("Ciphertext: ", ciphertext)
        elif mode == "decrypt":
            ciphertext = vigenere_decrypt(plaintext, key)
            print("Original text: ", ciphertext)
        else:
            print("Invalid mode, please choose 'encrypt' or 'decrypt'.")
    elif cipher == "playfair":
        key = input("Enter the key text: ")
        if mode == "decrypt":
            print("Decryption is not implemented in playfair ")
        elif mode == "encrypt":
            if len(key) < 5:
                print("Key must be at least 5 characters long.")
            ciphertext = encrypt_playfair(plaintext, key)
            print("Ciphertext: ", ciphertext)
    elif cipher == "affine":
        key = input("Enter the key text (in the form of 'a,b'): ")
        # Extracting the values of a and b from the key text
        key = key.replace("'", "")
        key = key.replace(" ", "")
        a, b = list(map(int, key.split(',')))
        if mode == "encrypt":
            ciphertext = encrypt_affine(plaintext, (a, b))
            print("Ciphertext: ", ciphertext)
        elif mode == "decrypt":
            plaintext = decrypt_affine(plaintext, (a, b))
            print("Plaintext: ", plaintext)
    else:
        print("Invalid cipher, please choose 'Caesar' or 'Vigenere' or playfair .")
