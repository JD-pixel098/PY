
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = 65
            else:
                base = 97

            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char

        else:
            result += char
    print(result)

caesar("hello" , 4)