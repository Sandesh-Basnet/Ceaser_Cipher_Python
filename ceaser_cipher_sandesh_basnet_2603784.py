def welcome():# Function to display a welcome message
    print("Welcome to the Caesar Cipher Program!")
    print("This program allows you to encrypt and decrypt messages using the Caesar cipher technique.")
    print("You can choose to shift letters by a specified number to encode or decode your messages.")
    print("Let's get started!")
welcome()
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
print(enter_message())
