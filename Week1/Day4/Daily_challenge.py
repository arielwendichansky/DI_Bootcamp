initial_values = str(('''    7ii
    Tsx
    h%?
    i #
    sM 
    $a 
    #t%
    ^r!'''))
lines = [line for line in initial_values.splitlines()]
print(lines)

matrixs = [list(line) for line in lines ]
print (matrixs)

for row in matrixs:
    print(row)

# res = [''.join(ele) for ele in matrixs]
# print(res)
message1 = [column[-3] for column in matrixs]
message2 = [column [-2] for column in matrixs]
message3 = [column [-1] for column in matrixs]
#
print (message1)
print (message2)
print (message3)
messages = message1 + message2 + message3
print (messages)
message = ''
alphabet = ("abcdefghijklmnopqrstuvwxyz^ ")
for i in messages:
    if i.lower() not in alphabet:
        continue
    else:
        message += str(i)
final_message = message.replace('^'," ")
print(final_message)

