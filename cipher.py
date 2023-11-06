# Function to encrypt text using Caesar cipher with right shift of 5
def caesar_cipher(text):
    encrypted_text = ""
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine whether the letter is uppercase or lowercase
            is_uppercase = char.isupper()
            # Shift the letter by 5 positions to the right
            shifted_char = chr((ord(char) - 65 + 5) % 26 + 65) if is_uppercase else chr((ord(char) - 97 + 5) % 26 + 97)
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char
    return encrypted_text

# Get input from the user
plain_text = input("Enter a plain text sentence: ")

# Encrypt the input text using Caesar cipher with right shift of 5
encrypted_text = caesar_cipher(plain_text)

# Print the encrypted text
print("Encrypted text: " + encrypted_text)
# add your code here
