"""
Author: Sandesh Basnet
Student ID: 2603784

Caesar Cipher Program
Encrypts and decrypts messages using the Caesar cipher technique.
"""


def welcome():
    """Display a welcome message."""
    print("Welcome to the Caesar Cipher Program!")
    print(
        "This program allows you to encrypt and decrypt messages "
        "using the Caesar cipher technique."
    )
    print(
        "You can choose to shift letters by a specified number "
        "to encode or decode your messages."
    )
    print("Let's get started!")


def enter_message():
    """Get user input for mode, message, and shift number."""
    mode = input("Enter 'e' to encrypt or 'd' to decrypt a message: ").lower()

    while mode not in ['e', 'd']:
        print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
        mode = input(
            "Enter 'e' to encrypt or 'd' to decrypt a message: "
        ).lower()

    message = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number (1-25): "))

    while shift < 1 or shift > 25:
        print("Invalid shift number. Please enter a number between 1 and 25.")
        shift = int(input("Enter the shift number (1-25): "))

    return mode, message, shift


def encrypt(message, shift):
    """Encrypt the message using the Caesar cipher technique."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ''

    for letter in message:
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + shift
                if new_index >= 26:
                    new_index -= 26
                ciphertext += letters[new_index]

    return ciphertext


def decrypt(message, shift):
    """Decrypt the message using the Caesar cipher technique."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''

    for letter in message:
        if letter != ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - shift
                if new_index < 0:
                    new_index += 26
                plaintext += letters[new_index]

    return plaintext


def is_file(filename):
    """Check if a file exists."""
    try:
        with open(filename, 'r', encoding='utf-8'):
            return True
    except IOError:
        return False


def process_file(filename, mode, shift):
    """Process messages from a file for encryption or decryption."""
    results = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().lower()
            if mode == 'e':
                results.append(encrypt(line, shift).upper())
            elif mode == 'd':
                results.append(decrypt(line, shift).upper())

    return results


def write_message(messages):
    """Write processed messages to a results file."""
    with open('results.txt', 'w', encoding='utf-8') as file:
        for message in messages:
            file.write(message + '\n')


def message_or_file():
    """Get user input for mode, source, and shift."""
    mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    while mode not in ['e', 'd']:
        print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

    choice = input(
        "Would you like to read from file (f) or console (c): "
    ).lower()

    while choice not in ['f', 'c']:
        print("Invalid input. Please enter 'f' for file or 'c' for console.")
        choice = input(
            "Would you like to read from file (f) or console (c): "
        ).lower()

    if choice == 'c':
        message = input("What message would you like to process: ").lower()
        shift = int(input("What is the shift number (1-25): "))

        while shift < 1 or shift > 25:
            print("Invalid shift number. Please enter a number between 1 and 25.")
            shift = int(input("What is the shift number (1-25): "))

        return mode, message, None, shift

    filename = input("Enter the filename (with extension): ")

    while not is_file(filename):
        print("Invalid filename")
        filename = input("Enter the filename (with extension): ")

    shift = int(input("What is the shift number (1-25): "))

    while shift < 1 or shift > 25:
        print("Invalid shift number. Please enter a number between 1 and 25.")
        shift = int(input("What is the shift number (1-25): "))

    return mode, None, filename, shift


def main():
    """Run the Caesar cipher program."""
    first_run = True

    while True:
        if first_run:
            welcome()
            first_run = False

        mode, message, filename, shift = message_or_file()

        if message is not None:
            if mode == 'e':
                encrypted_message = encrypt(message, shift)
                print("Encrypted Message:", encrypted_message.upper())
            elif mode == 'd':
                decrypted_message = decrypt(message, shift)
                print("Decrypted Message:", decrypted_message.upper())

        if filename is not None:
            results = process_file(filename, mode, shift)
            write_message(results)
            print("Output written to results.txt")

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("Exiting program!!!!!")
            break


main()
