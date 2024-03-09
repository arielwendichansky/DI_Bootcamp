"""list1 = [5, 10, 15, 20, 25, 50, 20]


find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


Hint : Look at the index method"""

list1 = [5, 10, 15, 20, 25, 50, 20]
print(list(enumerate(list1)))

for i,item in enumerate(list1):
    if item == 20:
        list1[i] = 200
        break
print(list1)



a=10
b=20
my_tuple=(a,b)
print(my_tuple)

c=a
d=b
my_tuple=(d,c)
print(my_tuple)

#Print the numbers from 1 to 10 using while loop

g=1
print(g)
while g < 10 :
    g+=1
    print(g)

# trying debug
secret_number = 4

while True:
    user_number= int(input("Guess the secret number: "))
    if user_number == secret_number:
        print("congrats!! you win!")
        break
    else:
        print ("wrong guess...")

#Access the value of key "history"
sample_dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

history_mark = sample_dict.get("class", {}).get("student", {}).get("marks", {}).get("history")

print("History Mark:", history_mark)

#Delete set of keys from Python Dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
print(sample_dict)
keys_to_remove = ["name", "salary"]

sample_dict.pop ("name")
sample_dict .pop ("salary")

print(sample_dict)







