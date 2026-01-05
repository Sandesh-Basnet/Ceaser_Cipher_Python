'''Author: Sandesh Basnet
Student ID: 2603784'''
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
def is_file(filename):# Function to check if a file exists
    try:
        with open (filename, 'r'):# Try to open the file in read mode
            return True# If successful, return True
    except:
        return False# If file does not exist, return False
def process_file(filename, mode, shift):# Function to process messages from a file for encryption or decryption
    results = []# List to store processed messages
    with open (filename, 'r') as file:# Open the specified file in read mode
        for line in file:# Iterate through each line in the file
            line = line.strip().lower()# Remove leading/trailing whitespace and convert to lowercase
            if mode == 'e':# If mode is encryption
                results.append(encrypt(line,shift).upper())# Append encrypted message in uppercase to results list
            elif mode == 'd':
                results.append(decrypt(line,shift).upper())# Append decrypted message in uppercase to results list
    return results
def write_message(messages):# Function to write processed messages to a results file
    with open ('results.txt','w') as file:# Open results.txt file in write mode
        for message in messages:# Iterate through each message in the messages list
            file.write(message + '\n')# Write each message to the file followed by a newline
def message_or_file():# Function to get user input for mode, message or filename, and shift number
    mode = input('Would you like to encrypt (e) or decrypt (d):').lower()# Get mode input from user
    while mode not in ['e','d']:# Validate mode input
        print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
        mode = input('Would you like to encrypt (e) or decrypt (d):').lower()
    choice = input("Would you like to read from file (f) or console (c):").lower()# Get input for message source
    while choice not in ['f','c']:# Validate choice input
        print("Invalid input. Please enter 'f' for file or 'c' for console.")
        choice = input("Would you like to read from file (f) or console (c):").lower()
    if choice == 'c':# If user chooses console input
        message = input("What message would you like to process:").lower()
        shift = int(input("What is the shift number (1-25):"))
        while shift < 1 or shift > 25:# Validate shift input
            print("Invalid shift number. Please enter a number between 1 and 25.")
            shift = int(input("What is the shift number (1-25):"))
        return mode, message, None, shift# Return mode, message, None for filename, and shift
    elif choice == 'f':# If user chooses file input
        filename = input("Enter the filename (with extension):")# Get filename input from user
        while not is_file(filename):# Validate if file exists
            print("Invalid filename")# Prompt user until a valid filename is provided
            filename = input("Enter the filename (with extension):")# Get filename input from user
        shift = int(input("What is the shift number (1-25):"))
        while shift < 1 or shift > 25:# Validate shift input
            print("Invalid shift number. Please enter a number between 1 and 25.")
            shift = int(input("What is the shift number (1-25):"))
        return mode, None, filename, shift# Return mode, None for message, filename, and shift
def main():# Main function to run the Caesar cipher program
    first_run = True# Variable to track if it's the first run of the program
    while True:# Loop to allow multiple encryptions/decryptions
        if first_run == True:# Display welcome message only on the first run
            welcome()# Display welcome message
            first_run = False# Set first_run to False after displaying the welcome message
        mode, message, filename, shift = message_or_file()# Get user inputs for mode, message, and shift number
        if message != None:# If message is provided (not from file)
            if mode == 'e':# If mode is encryption
                encrypted_message = encrypt(message, shift)# Encrypt the message
                print("Encrypted Message:", encrypted_message.upper())# Display encrypted message in uppercase
            elif mode == 'd':# If mode is decryption
                decrypted_message = decrypt(message, shift)# Decrypt the message
                print("Decrypted Message:", decrypted_message.upper())# Display decrypted message in uppercase
        if filename != None:# If filename is provided (message from file)
            results = process_file(filename,mode,shift)# Process messages from the file
            write_message(results)# Write processed messages to results.txt
            print("Output written to results.txt")# Notify user that output has been written to results.txt
        choice = input("Do you want to continue? (y/n): ").lower()# Ask user if they want to continue
        if choice != 'y':# If user chooses not to continue, exit the program
            print("Exiting program!!!!!")
            break# Exit the loop and end the program
main()