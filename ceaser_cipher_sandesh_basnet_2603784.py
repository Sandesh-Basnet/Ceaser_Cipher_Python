def welcome():# Function to display a welcome message
    print("Welcome to the Caesar Cipher Program!")
    print("This program allows you to encrypt and decrypt messages using the Caesar cipher technique.")
    print("You can choose to shift letters by a specified number to encode or decode your messages.")
    print("Let's get started!")
def enter_message():# Function to get user input for mode, message, and shift number
    mode = input("Enter 'e' to encrypt or 'd' to decrypt a message: ").lower()
    while mode not in ['e', 'd']:# Validate mode input
        print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
        mode = input("Enter 'e' to encrypt or 'd' to decrypt a message: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number (1-25): "))
    while shift < 1 or shift > 25:# Validate shift input
        print("Invalid shift number. Please enter a number between 1 and 25.")
        shift = int(input("Enter the shift number (1-25): "))
    return mode, message, shift#Returns user inputs for further processing
letters = 'abcdefghijklmnopqrstuvwxyz'# String containing all lowercase letters for reference
def encrypt(message,shift):# Function to encrypt the message using Caesar cipher technique
    ciphertext = ''
    for letter in message:# Iterate through each letter in the message
        if not letter == ' ':# Check if the letter is not a space
            index  = letters.find(letter)# Find the index of the letter in the letters string
            if index == -1:# If letter is not found in letters string, keep it unchanged
                ciphertext +=letter
            else:# If letter is found, perform the shift operation
                new_index = index + shift# Calculate new index after applying the shift
                if new_index >=26:# Wrap around if new index exceeds 25
                    new_index -= 26# Adjust new index to stay within bounds
                ciphertext += letters[new_index]# Append the shifted letter to ciphertext
    return ciphertext
def decrypt(message,shift):
    plaintext =''
    for letter in message:
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext +=letter
            else:
                new_index = index -shift
                if new_index <0:
                    new_index += 26
                plaintext += letters[new_index]
    return plaintext
