def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabet characters remain unchanged
        else:
            encrypted_text += char

    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    # Decryption is simply the reverse of encryption
    return caesar_cipher_encrypt(text, -shift)


def main():
    print("---- Ceaser Cipher ---- Encryption & Decryption ----")
    
    # User input for message and shift value
    message = input("Enter the message--> ")
    shift = int(input("Enter the shift value--> "))

    #User choose if he wants to decrypt a message
    print("Do you want to do encryption or decryption??")
    choice = input ("E--> Encryption | D--> Decryption --> ")

    if choice == 'E':
        # Encrypt the message
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    
    elif choice == 'D':
        # Decrypt the message
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    
    else:
        print("Invalid Entry")

if __name__ == "__main__":
    main()
