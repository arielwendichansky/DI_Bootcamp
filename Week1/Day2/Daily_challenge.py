"""
Challenge 1
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
Examples

number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]


Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Notes
Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

"""

# Exercise_1
list=[]
number = int(input("provide me a number: "))
length = int(input("provide me a lenght: "))
list.append(number)

while len(list) < length:
        number *= 2
        list.append(number)

print(list)

print(">"*30)

#Exercise_2
string = input("share a string: ")
duplicates = []


for index,letter in enumerate(string):
        if index == 0 or letter != string[index - 1]:
                duplicates.append(letter)

word = ''.join(duplicates)
print(word)

