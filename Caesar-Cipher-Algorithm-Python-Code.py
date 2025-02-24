# Caesar Cipher Implementation in Python

def caesar_cipher(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    result = ""

    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            is_upper = char.isupper()
            alphabet_start = ord('A') if is_upper else ord('a')

            # Shift the character and wrap around using modulo
            shifted_char = chr((ord(char) - alphabet_start + shift) % 26 + alphabet_start)
            result += shifted_char
        else:
            # Non-alphabetic characters are added as it is
            result += char

    return result

# User Interaction
print("Welcome to the Caesar Cipher Implementation Program !!!")
print("-------------------------------------------------------\n")
while True:
    mode = input("Do you want to 'Encrypt' or 'Decrypt' a message? (type 'Exit' to quit): ").lower()
    if mode == "exit":
        print("Thank You !!!")
        break
    elif mode not in ["encrypt", "decrypt"]:
        print("Invalid choice. Please type 'encrypt', 'decrypt', or 'exit'.")
        continue

    text = input("\nEnter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer. Try again.")
        continue
    result = caesar_cipher(text, shift, mode)
    if mode == "encrypt":
        print("\nThe Encrypted Message is: ",result)
    if mode == "decrypt":
        print("\nThe Decrypted Message is: ",result)