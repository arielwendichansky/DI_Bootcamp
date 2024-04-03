# Ex_1: Write a script that inserts an item at a defined index in a list.
str_input = input("What you want to say? ")
list_input = str_input.split(' ')
print(list_input)
chrc_input = input("Which character you want to add? ")
chrc_index = int(input("where you want to index it? (only numbers) "))
str_answ = ""

for count, ele in enumerate(list_input):
    if count == chrc_index:
        str_answ += chrc_input + " " + ele + " "
    else:
        str_answ += ele + " "

print(str_answ.strip())

# Ex_2:  Write a script that counts the number of spaces in a string.
space_count = 0
for i in str_input:
    if i == ' ':
        space_count += 1
print(f"The total number of spaces is {space_count}")

# Ex_3: Write a script that calculates the number of upper case letters and lower case letters in a string.
upper_count = 0
lower_count = 0
for i in str_input:
    if i.isupper():
        upper_count += 1
    else:
        lower_count += 1
print(f"In your string there are {upper_count} upper cases and {lower_count} cases")

# Ex_4: Write a function to find the sum of an array without using the built-in function:

chrc_input = int(input("How many values you want to add? "))
my_sum = []
chrc_count = 0
result = 0

while chrc_count != chrc_input:
    num_input = int(input("Input value:\n>>> "))
    my_sum.append(num_input)
    chrc_count += 1
for n in my_sum:
    result += n
print(f"Here the list of values inserted {my_sum}.\nThe sum of them is {result}")
#
# # Ex_5: Write a function to find the max number in a list
print(f"The highest value in list {my_sum} is {max(my_sum)}")

# Ex_6: Write a function to find the max number in a list
fact_num = int(input("Which number you want to factorize? "))
fact = 1
for i in range(1, fact_num+1):
    fact *= i
print(fact)

# Ex_7: Write a function that counts an element in a list (without using the count method)

list_count = (['a', 'a', 't', 'o'], 'a')
counter = 0
for i in list_count:
    for j in i:
        counter += 1

print(f"There are {counter} elements  in the list provided")

# Ex_8: Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

norm = ([1, 2, 2])
sum = 0
for i in norm:
    sum += i ** 2
result = sum ** 0.5
print(int(result))

# Ex_9: Write a function to find if an array is monotonic (sorted either ascending of descending)

is_mono1 = ([7, 6, 5, 5, 2, 0])

is_mono1_asc = sorted(is_mono1)
is_mono1_desc = sorted(is_mono1, reverse=True)

if is_mono1 == is_mono1_asc or is_mono1 == is_mono1_desc:
    print(True)
else:
    print(False)

is_mono2 = ([1, 2, 0, 4])

is_mono2_asc = sorted(is_mono2)
is_mono2_desc = sorted(is_mono2, reverse=True)

if is_mono2 == is_mono2_asc or is_mono2 == is_mono2_desc:
    print(True)
else:
    print(False)

# Ex_10: Write a function that prints the longest word in a list.

string_list = ['hello', 'the', 'common', 'unique', 'best']
longest_word = ""
for i in string_list:
    if len(i) > len(longest_word):
        longest_word = i
print(f"Longest word in list is {longest_word}")

# Ex_11: Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

lists = ['hello', 'the', 'common', 'unique', 'best', 1, 2, 3]
string_list = []
num_list = []
for i in lists:
    if type(i) is str:
        string_list.append(i)
    elif type(i) is int:
        num_list.append(i)
print(string_list)
print(num_list)


# Ex_12: Write a function to check if a string is a palindrome:

def is_palindrome(inp_string):
    if inp_string[0] == inp_string[-1]:
        print(f"The word is palindrome")
    else:
        print('The word is not palindrome')


is_palindrome('John')

# Ex_13: Write a function that returns the amount of words in a sentence with length > k

sentence = 'Do or do not there is no try'
k = 2


def sum_over_k(sentence, k):
    counter = 0
    sentence_list = sentence.split()
    for i in sentence_list:
        if len(i) > k:
            counter += 1
    return print(f"The amount of words in a sentence with length > k is {counter}")


sum_over_k(sentence, k)


# Ex_14: Write a function that returns the average value in a dictionary (assume the values are numeric):


def dict_avg(dic):
    counter = 0
    iteration = 0
    for i, j in dic.items():
        counter += j
        iteration += 1
    return print(f"Avg result is {int(counter / iteration)}")


dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1})


# Ex_15: Write a function that returns common divisors of 2 numbers:

def common_div(num1, num2):
    common = []
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == num2 % i == 0:
            common.append(i)
    return common


result = common_div(10, 20)

print(result)


# Ex_16: Write a function that test if a number is prime:

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


result = is_prime(11)
print(result)


# Ex_17: Write a function that prints elements of a list if the index and the value are even:
def weird_print(list):
    even_num = []
    if len(list) % 2 == 0:
        for i in list:
            if i % 2 == 0 and i not in even_num:
                even_num.append(i)
    else:
        print(f"The list provided is not even, length of the list is {len(list)}")
    return even_num


result = weird_print([1, 2, 2, 3, 4, 5])

print(result)


# Ex_18: Write a function that accepts an undefined number of keyword and return the count of different types:

def type_count(**kwargs):
    counts = {}
    for value in kwargs.values():
        # Get the type of the value
        val_type = type(value).__name__
        # Count the occurrence of this type
        counts[val_type] = counts.get(val_type, 0) + 1
    return counts


result = type_count(a=1, b='string', c=1.0, d=True, e=False)
for key, value in result.items():
    formatted_result = ','.join(f"{key}: {value}" for key, value in result.items())
print(formatted_result)


# Ex_19: Write a function that mimics the builtin .split() method for strings
def split_func(string, object):
    output = []
    wrd = ''
    for i in string:
        if i == ' ':
            output.append(wrd)
            output.append(object)
            wrd = ''
        else:
            wrd += i
    if wrd:  # If there's any leftover word after the loop
        output.append(wrd)
    return output


result = split_func('Hola como estas?', 'o')
print(result)
# Ex_20: Convert a string into password format.

input_psw = input("password: ")
input_len = len(input_psw)
output = '*' * input_len
print(f"output: {output}")
