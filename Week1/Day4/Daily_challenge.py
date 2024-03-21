initial_values = str(('''    7ii
    Tsx
    h%?
    i #
    sM 
    $a 
    #t%
    ^r!'''))
lines = [line for line in initial_values.splitlines()]

matrixs = [list(line) for line in lines ]

for row in matrixs:
    print(row)

message1 = [column[-3] for column in matrixs]
message2 = [column [-2] for column in matrixs]
message3 = [column [-1] for column in matrixs]

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

