from random import randint


def encrypt(text, shift):
    result = ""

    for i in range(len(text)):  # 0 1 2 3
        char = text[i]

        if (ord(char) < 65 or ord(char) > 122) or (91 <= ord(char) <= 96):
            result += chr(ord(char))
        else:

            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


def decrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (ord(char) < 65 or ord(char) > 122) or (91 <= ord(char) <= 96):
            result += chr(ord(char))
        else:

            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)

    return result




def brute_force(encrypted_text):
    for i in range(1, 26):
        text = decrypt(encrypted_text, i)
        print("Shift :" + str(i) + " " + text)
        
        elif choice == 2:
    input_text = input("Your text: ")
    method = int(input("Press 1 to decrpyt with specific key\nPress 2 to bruteforce\nChoose method :"))
    if method == 1 or method == 2:
        if method == 1:
            specific_key = int(input("Key: "))
            decrypted_text = decrypt(input_text, specific_key)
            print("Decrypted text with shift: " + str(specific_key) + " is :" + decrypted_text)

        else:
            brute_force(input_text)
    else:
        print(




print("Welcome. \nPress 1 to encrypt text\nPress 2 to decrpyt")
choice = int(input("Your choice is : "))

if choice == 1:
    input_text = input("Your text: ")
    random = int(input("Press 1 to encrypt with random key\nPress 2 to encrypt with specific key\nYour choice: "))
    if random == 1 or random == 2:
        if random == 1:
            input_shift = randint(1, 26)
        else:
            input_shift = int(input("Shift: "))
        encrypted_text = encrypt(input_text, input_shift)
        print("Encrypted text with shift: " + str(input_shift) + " is :" + encrypted_text)

    else:
        print("WRONG INPUT")





