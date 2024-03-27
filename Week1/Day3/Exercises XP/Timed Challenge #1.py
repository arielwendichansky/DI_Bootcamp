# Write a program to reverse the sentence wordwise.
input_string = 'You have entered a wrong domain'
input_list = input_string.split(' ')
input_backwards = ""
while input_list:
    input_backwards += input_list.pop() + " "
print(input_backwards)