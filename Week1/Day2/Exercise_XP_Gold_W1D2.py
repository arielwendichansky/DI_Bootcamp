# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.
#
#
# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
#
#
# Exercise 3: Check The Index
# Instructions
# Using this variable
#
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1
#
#
# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87
#
#     The greatest number is: 87
#
#
# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
#
#
# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
#
#
# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
#
#
# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
#
# Then, the output should be:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
#
# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

#Exercise 1
list1 = []
list2 = []

for i in list2:
    list1.append(i)

#Exercise 2
multiples_5 = []
multiples_7 = []

for i in range(1500, 2501):
    if i % 5 == 0:
        multiples_5.append(i)
    elif i % 7 == 0:
        multiples_7.append(i)
print(f"these are the multiples from 5: {multiples_5}")
print(f"these are the multiples from 7: {multiples_7}")

#Exercise3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name_input = input("What's your name? ")
name_title = name_input.title()
for name in names:
    if name == name_title:
        name_index = names.index(name_title)
    else:
        names.append(name_title)
print(name_index)

#Exercise4

first_number = int(input("Input the 1st number: "))
second_number = int(input("Input the 2nd number: "))
third_number = int(input("Input the 3rd number: "))
numbers = [first_number,second_number,third_number]

greatest_number = max(numbers)
print(f"The greatest number is: {greatest_number}")

#Exercise5

alphabet =('abcdefghijklmnopqrstuvwxyz')
vowels = ['a', 'e','i','o','u']
vowels_alphabet = []
consonant = []

for i in alphabet:
        if i in vowels:
            vowels_alphabet.append(i)
        else:
            consonant.append(i)

print(vowels_alphabet)
print(consonant)
#
# #Exercise 6
#
input_words_list = []
input_letters_list = []

while len(input_words_list) < 7:
    input_word = input("please input a word: ")
    input_words_list.append(input_word)

input_letter = input("please input a letter: ")
input_letters_list.append(input_letter)

for word in input_words_list:
    index = word.find(input_letter)
    if index != -1:
        print(f"The first appearance of '{input_letter}' in '{word}' is at index {index}")
    else:
        print(f"The chosen letter {input_letter} doesn't appears in the word {word}")


#Exercise 7
list_numbers = []
for n in range(1, 1000001):
    list_numbers.append(n)

min_numb = min(list_numbers)
print(min_numb)
max_numb = max(list_numbers)
print(max_numb)
sum_numbers = sum(list_numbers)
print(sum_numbers)

#Exercise 8
list_numbers = []
while True:
    print("If you want to input a number press 1 to exit 2")
    ans = int(input(">>> "))
    if ans == 1:
        input_ans = input("Please input values: ")
        raw_list = input_ans.split(',')
        list_numbers = [number for number in raw_list if number.isdigit()]
    elif ans == 2:
        print(f"Here the list and tuple:\nList: {list_numbers}\nTuple:{tuple(list_numbers)}")
        break
    else:
        print("You can ony introduce 1 or 2")

#Exercise 9
import random

while True:
    user_ans = int(input("Please input a number from 1 to 9:\n>>> "))
    if user_ans in range(1,10):
        random_num = random.choice(range(1, 10))
        if user_ans == random_num:
            print(f"You won!! the random number is {random_num}!!")
            break
        else:
            print(f"I'm sorry you lost, the random number is {random_num}")
            break
    else:
        print("Number has to be in range from 1 to 9")

