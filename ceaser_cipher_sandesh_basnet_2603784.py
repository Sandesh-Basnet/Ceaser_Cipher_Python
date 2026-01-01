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
    message = input("Enter your message: ").lower()# Get message input and convert to lowercase
    shift = int(input("Enter the shift number (1-25): "))
    while shift < 1 or shift > 25:# Validate shift input
        print("Invalid shift number. Please enter a number between 1 and 25.")
        shift = int(input("Enter the shift number (1-25): "))
    return mode, message, shift#Returns user inputs for further processing
def encrypt(message,shift):# Function to encrypt the message using Caesar cipher technique
    letters = 'abcdefghijklmnopqrstuvwxyz'# String containing all lowercase letters for reference
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
def decrypt(message,shift):# Function to decrypt the message using Caesar cipher technique
    letters = 'abcdefghijklmnopqrstuvwxyz'# String containing all lowercase letters for reference
    plaintext =''
    for letter in message:# Iterate through each letter in the message
        if not letter == ' ':# Check if the letter is not a space
            index = letters.find(letter)# Find the index of the letter in the letters string
            if index == -1:# If letter is not found in letters string, keep it unchanged
                plaintext +=letter
            else:# If letter is found, perform the reverse shift operation
                new_index = index -shift# Calculate new index after reversing the shift
                if new_index <0:# Wrap around if new index is negative
                    new_index += 26# Adjust new index to stay within bounds
                plaintext += letters[new_index]# Append the shifted letter to plaintext
    return plaintext
def main():# Main function to run the Caesar cipher program
    welcome()# Display welcome message
    mode, message, shift = enter_message()# Get user inputs
    if mode == 'e':# If mode is encryption
        encrypted_message = encrypt(message, shift)# Encrypt the message
        print("Encrypted Message:", encrypted_message.upper())# Display encrypted message in uppercase
    elif mode == 'd':# If mode is decryption
        decrypted_message = decrypt(message, shift)# Decrypt the message
        print("Decrypted Message:", decrypted_message.upper())# Display decrypted message in uppercase
main()