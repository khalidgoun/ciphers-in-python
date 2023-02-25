I've created a Python program that allows users to choose from several popular ciphers, including Caesar, Vigenere, Playfair, and Affine. Encryption and decryption are 
essential components of secure communication, and this program provides a user-friendly way to experiment with various ciphers.

The program prompts users to input a key for the selected cipher and to select an encryption mode (encryption or decryption). Users can enter their own message to be 
encrypted or decrypted, or they can choose to use a default message provided by the program.

In addition to the popular ciphers, the program includes a function to encrypt text using the Playfair cipher. This function converts the text to lowercase, 
removes spaces, groups the text into diagraphs, and fills in any necessary letters. It then generates a 5x5 key square matrix based on the input key and uses this
matrix to encrypt the text using the Playfair cipher algorithm.
