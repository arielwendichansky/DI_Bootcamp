C = 50
H = 30
Q = []
D = list(map(int, input("Input the numbers separated by comma: ").split(',')))

for i in D:
    q = ((2 * C * i)/H) ** 0.5
    q_rounded = round(q, None)
    Q.append(str(q_rounded))
print(','.join(Q))

print('>'*30)

# Exercise 2

l1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
l2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
l3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
l4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
final_list = l1 + l2 + l3 + l4
print(final_list)
sort_final_list = sorted(final_list, reverse=True)
print(sort_final_list)
sum_final_list = sum(final_list)
print(sum_final_list)
start_end = (final_list[0],final_list[-1])
print(start_end)
list_greater_50 = [num for num in final_list if num > 50]
print(list_greater_50)
list_smaller_10 = [num for num in final_list if num < 10]
print(list_smaller_10)
squared = [num**2 for num in sort_final_list]
print(squared)
set_list = set(sort_final_list)
print(len(set_list))
avg_num = (sum_final_list/len(final_list))
print(avg_num)
largest_smallest = (sort_final_list[0],sort_final_list[-1])
print(largest_smallest)

print('>'*30)

# Exercise 3

paragraph = ("Bootcamps provide intensive learning experiences in fields like software development and data science.\n"
             "With hands-on projects and industry mentorship, students gain in-demand skills quickly.\n"
             "Career-focused services help graduates secure employment in tech and digital industries.")
print(f"This is an intro to what a Bootcamp is.\n{paragraph}")

characters = len(paragraph)
print(characters)

sentences = [sentence.strip() for sentence in paragraph.split('\n') for sentence in sentence.split('.') if sentence.strip()]
print(len(sentences))

words = print(len(paragraph.split()))

unique_words = set(paragraph.split())
print(len(unique_words))

print('>'*30)

# Exercise 4

text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = text.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] = 1
for frequence, count in frequency.items():
    print(frequence, count)
print(frequency)
