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
