# decrypt ceaser cipher

def decrypt(text, shift):
    res = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            res += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            res += chr((ord(char) - shift - 97) % 26 + 97)

    return res


userInput = input("Enter the string to encrypt: ")
shift = int(input("Enter the character shift: "))

print(decrypt(userInput, shift))
