# Create a python program that encrypts and decrypts messages with Caesar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt,
# and then execute encryption/decryption on a given message and a given shift.

text = input("What phrase you want to encrypt? ")
# abc = 'abcdefghijklmnopqrstuvwxyz'
# abc = {letter:value for value, letter in enumerate(abc)}
cypher_text = ""
for letter in text:
    if letter.lower() == 'z':
        cypher_text += 'c'
    elif letter.lower() == 'y':
        cypher_text += 'b'
    elif letter.lower() == 'x':
        cypher_text += 'a'
    else:
        cypher_text += chr(ord(letter) + 3)

print(cypher_text.replace('#', ' '))

while True:
    decrypt = ""
    answ = int(input("You want to decrypt the text?\n1 = Yes\n2 = No\n>>> "))
    if answ == 1:
        for letter in cypher_text:
            if letter.lower() == 'c':
                decrypt += 'z'
            elif letter.lower() == 'b':
                decrypt += 'y'
            elif letter.lower() == 'a':
                decrypt += 'x'
            else:
                decrypt += chr(ord(letter) - 3)
        print(f"The original message is {decrypt}")
        break
    else:
        break
