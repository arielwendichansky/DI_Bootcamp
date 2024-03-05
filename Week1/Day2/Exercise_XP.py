""""🌟 Exercise 1 : Set
Instructions
Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.


🌟 Exercise 2: Tuple
Instructions
Given a tuple which value is integers, is it possible to add more integers to the tuple?


🌟 Exercise 3: List
Instructions
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)


🌟 Exercise 4: Floats
Instructions
Recap – What is a float? What is the difference between an integer and a float?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
Can you think of another way to generate a sequence of floats?


🌟 Exercise 5: For Loop
Instructions
Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.


🌟 Exercise 6 : While Loop
Instructions
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


🌟 Exercise 7: Favorite Fruits
Instructions
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.


Exercise 8: Who Ordered A Pizza ?
Instructions
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


Exercise 9: Cinemax
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.


Exercise 10 : Sandwich Orders
Instructions
Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
We need to prepare the orders of the clients:
Create an empty list called finished_sandwiches.
One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
I made your tuna sandwich
I made your avocado sandwich
I made your egg sandwich
I made your chicken sandwich
"""


#Exercise_1
my_fav_numbers = set()
my_fav_numbers.add(1)
my_fav_numbers.add(2)
my_fav_numbers.add(4)
print(my_fav_numbers)
my_fav_numbers.remove(4)
print(my_fav_numbers)
friend_fav_numbers = set()
friend_fav_numbers.add(20)
friend_fav_numbers.add(23)
friend_fav_numbers.add(10)
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

print(">"*30)
#Exercise_2

print("Given a tuple which value is integers, is it possible to add more integers to the tuple?")
print("The answer is no, as tuples are immutable, they can't be changed, but we can create a new variable and add the values from this tuple that was created. Although, the original one will remain the same.  ")

print(">"*30)
#Exercise_3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]


print(basket)
basket.pop(0)
basket.pop(-1)
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket)

apple = basket.count("Apples")
print(f"There are {apple} Apples in the basket")

basket.clear()
print(f"There are {basket} objects in the basket")

print(">"*30)
#Exercise_4

# A float is a number with decimal place, not integer. Float is mainly used when we need more precision in the input values.

my_list = []
first = 1
while first < 5:
    first += 0.5
    my_list.append(first)

print(my_list)

print(">"*30)
#Exercise_5

numbers = range(1,21)
for number in numbers:
    print(number)

print(">"*6)

for number in numbers:
    if number % 2 ==0:
        print (number)

print(">"*30)
#Exercise_6

name = ""
while name != "Ariel":
    name = input("Please insert your name: ")
print("you chose the correct name!!")

print(">"*30)
#Exercise_7

list_fruit = []

list_fruit = input("Choose as many fruits you like, separated by a single space: ")
list_fruit = list_fruit.split()
print(list_fruit)

new_fruit = input("Give me the name of a fruit: ")

if new_fruit in list_fruit:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")

print(">"*30)
#Exercise_8

pizza_toppings = []
pizza_topping = ""

while pizza_topping != "quit":
    pizza_topping = input("Which topping you want for your pizza? If you don't want more just intro quit ")
    if pizza_topping == "quit":
        break
    else:
        pizza_toppings.append(pizza_topping)
for toppings in pizza_toppings:
    price = 10 + float((2.5) * len(pizza_toppings))

print(f"You chose the following topics: {pizza_toppings}")
print(f"The price of the pizza is ${price}")


print(">"*30)

#Exercise_9

ticket = 0
total_price = 0
age = 0
ages = []
buy = ""
total_tickets = 0

while True:
    buy = input("Welcome! enter 'Y' to buy a new or continue buying ticket/s or 'N' if you want to exit: ")

    if buy == "N":
        print("Thanks for coming to the cinema!")
        break
    elif buy != "Y":
        print("Invalid input. Please enter 'Y' or 'N'.")
        continue
    total_tickets = int(input("How many ticket you want to buy? "))

    while ticket != total_tickets:
        age = int(input("How old is the attendee? "))
        ages.append(age)
        ticket = int(len(ages))
        if age <= 3:
            price = 0
        elif 3 < age <= 12:
            price = 10
            total_price += price
        elif age > 12:
            price = 15
            total_price += price


print(f"The total price to pay is ${total_price}")

print(">"*6)

names = []
age = 0
name=""
while True:
    age = int(input("How old are you? "))
    if 16 <= age <= 21:
        name = input("What is your name? ")
        names.append(name)
        continue
    else:
        print("You are not allowed to watch this movie")
    break
print(names)

print(">"*30)

#Exercise_10

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")


while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    str(print("I made your " + sandwich))