def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
