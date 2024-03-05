"""Exercise 1 : Hello World
Instructions
Print the following output in one line of code:

Hello world
Hello world
Hello world
Hello world


Exercise 2 : Some Math
Instructions
Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).


Exercise 3 : What Is The Output ?
Instructions
Predict the output of the following code snippets:
#>>> 5 < 3
#>>> 3 == 3
#>>> 3 == "3"
#>>> "3" > 3
#>>> "Hello" == "hello"


🌟 Exercise 4 : Your Computer Brand
Instructions
Create a variable called computer_brand which value is the brand name of your computer.
Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".


🌟 Exercise 5 : Your Information
Instructions
Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code


🌟 Exercise 6 : A & B
Instructions
Create two variables, a and b.
Each variable value should be a number.
If a is bigger then b, have your code print Hello World.


Exercise 7 : Odd Or Even
Instructions
Write code that asks the user for a number and determines whether this number is odd or even.


🌟 Exercise 8 : What’s Your Name ?
Instructions
Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.


🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
Instructions
Write code that will ask the user for their height in inches.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride."""

#Exercise_1
print(('Hello world'+ '\n' )*5)

print('>'*30)
#Exercise_2
result= (99^3)*8
print(result)

print('>'*30)
#Exercise_3
""">>> 5 < 3 #False
>>> 3 == 3 #True
>>> 3 == "3" #False
>>> "3" > 3 #False
>>> "Hello" == "hello" #False"""

#Exercise_4

computer_brand = input('Which is the brand name of your computer? ')
print(f"I have a {computer_brand} computer")

print('>'*30)
#Exercise_5

name = input('Whats your name? ')
age = input('Whats your age? ')
shoe_size = input('Whats your shoe_size? ')
info = (f'My name is {name}, Im {age} yo and my feet are {shoe_size} cm long')
print(info)

print('>'*30)
#Exercise_6
a = input('Give me a number: ')
b = input('Give me another number: ')

if a > b:
    print ('Hello World')
else:
    print('Second number is bigger than 1st')

print('>'*30)
#Exercise_7

number = int(input('Give me a number: '))
if number % 2 == 0 :
    print('This is an odd number')
else:
    print("You've selected a even number")

print('>' * 30)
# Exercise_8

name_1 = str(input('Whats your name? '))
if name_1 == 'Ariel' :
    print('Congrats you have a great name!!')
else:
    print('Im sorry your name is not as cool as Ariel')

print('>' * 30)
# Exercise_9

height = float(input('Whats your height in cm? '))
if height > 1.45:
    print("Congrats you're tall enough to ride!!")
else:
    print('Im sorry you need to grow some more to ride')
