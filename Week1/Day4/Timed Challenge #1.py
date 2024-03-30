# Write a program which takes a string and a character as an input,
# and finds out the number of occurrences the character has in the string.

string = input("Write a string :")
chrct = input("Which letter you want to count in your sting? ")
chrct_sum = 0

for i in string:
    if i.lower() == chrct:
        chrct_sum += 1
print(f"String: {string}")
print(f"Searched character: {chrct}")
print(f"The number of occurrences the character has in the string is {chrct_sum}")



