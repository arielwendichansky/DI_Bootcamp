# Exercise 1: Birthday Look-Up
birthdays = {}

while len(birthdays) <= 4:
    name = input("Name of the birthday person:")
    date = input("Birthday from the birthday person (YYYY/MM/DD): ")
    birthdays[name] = date

print(birthdays)

query_name = input(" Whose birthday are you looking for?")
for k,v in birthdays.items():
    if k == query_name:
        print(f"The birthday date from {query_name} is {v}")
        break
    else:
        print("the person you are looking for is not in the list")

# Exercise 2: Birthdays Advanced

birthdays = {'Ariel':'1994/02/02','Martina':'1998/04/20','Eliana':'1996/09/21','Julieta':'1992/08/16','Pablo':'1960/11/12' }
print(birthdays)
query_name = input(" Who's birthday you are looking for?")
for k,v in birthdays.items():
    if k == query_name.title():
        print(f"The birthday date from {query_name.title()} is {v}")
        break
    else:
        print(f"Sorry, we don’t have the birthday information for {query_name}")
        break

# Exercise 3: Add Your Own Birthday

birthdays = {}


name = input("Name of the birthday person:")
date = input("Birthday from the birthday person (YYYY/MM/DD): ")
birthdays[name] = date

query_name = input(" Whose birthday are you looking for?")
for k,v in birthdays.items():
    if k == query_name:
        print(f"The birthday date from {query_name} is {v}")
        break
    else:
        print("The person you are looking for is not in the list")
        break

# Exercise 4: Fruit Shop

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
output = ''
for k, v in items.items():
    output += f"{k}:{v} "

print(f"Welcome to our fruits store, we have the following fruits for you:\n"
      f"{output}")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_price = 0
for k,v in items.items():
        total_price += v['price']*v['stock']
print(total_price)
