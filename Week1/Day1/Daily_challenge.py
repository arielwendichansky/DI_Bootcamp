

"""Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

Then, print the first and last characters of the given text.

Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld


4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

Hlrolelwod"""

#Exercise_1

a = input("Input a sentence of just 10 characters: ")
if len(a) < 10:
    print("string not long enough")
elif len(a) > 10:
    print("string too long")
else:
    print("perfect string")

print('>' * 30)
# Exercise_2

print (a[0])
print(a[-1])

print('>' * 30)
# Exercise_3

b = 'Hello World'
c = ''
for i in b:
    c += i
    print(c)

print('>' * 30)
# Exercise_4

import random

pre_list = list (b)
random.shuffle(pre_list)
final_list =''.join(pre_list)
print(final_list)


