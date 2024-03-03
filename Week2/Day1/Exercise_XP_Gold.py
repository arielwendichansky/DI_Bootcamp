"""Exercise 1 : Hello World-I Love Python
Instructions
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
I love python
I love python
I love python
I love python


Exercise 2 : What Is The Season ?
Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
"""

print('>' * 30)
# Exercise_1

print(("Hello World" + "\n")*4 + ("I love Python" + "\n" )*4)

print('>' * 30)
# Exercise_2

month = int(input("1 - January"+ '\n'
                  "2 - February" + '\n'
                  "3 - March"+ '\n'
                  "4 - April" + '\n'
                  "5 - May" + '\n'
                  "6 - June"+ '\n'
                  "7 - July"+ '\n'
                  "8 - August"+ '\n'
                  "9 - September"+ '\n'
                  "10 - October"+ '\n'
                  "11 - November"+ '\n'
                  "12 - December"+ '\n'
                  "Select the number of the month from the list:"))
if month in [3, 4, 5]:
    print("Is the Spring time!")

elif month in [6, 7, 8]:
    print("Is the Autumn time!")

elif month in [9, 10, 11]:
    print("Is the Winter time!")

elif month in [1, 2, 12]:
    print("Is the Summer time!")

else:
    print("You've selected a wrong month or value")


