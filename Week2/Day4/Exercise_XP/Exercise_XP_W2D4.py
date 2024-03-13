#Exercise 1
import os
import random

from faker import Faker

sentence_lenght = int(input("How long does the sentence should be? "))
# fake = Faker()
# fake_sentence = fake.text(max_nb_chars=sentence_lenght)
# print(fake_sentence)


dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path+'\\sowpods.txt')

def get_words_from_file():
    with open(dir_path + '\\sowpods.txt', 'r') as file_obj:
        words_in_file = file_obj.read().splitlines()
        # string_words = ", ".join(words_in_fle)
    return  words_in_file


def get_random_sentence (sentence_lenght):
    list_of_words = get_words_from_file()
    sentence = " ".join(random.choices(list_of_words,k=sentence_lenght)).lower()
    print(sentence)

def main():
    possible_values = range(2,21)
    try:
        if sentence_lenght in possible_values:
            print(f"The program extracts random words from this file {dir_path+'\\sowpods.txt'} \n"
                  f"Then it will provide you a list of sentence with the length you've selected {sentence_lenght}:")
            get_random_sentence(sentence_lenght)
        else:
            raise ValueError("Lenght of the value has to be between 2 and 20")
    except ValueError as e:
        print(e)


main()

#Exercise 2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_file = 'emmajson.json'
#running the json into a file writting it
with open (json_file,'w') as file_obj:
    json.dump(sampleJson,file_obj)
#reading the json file and dumping the files into a file content
with open(json_file, 'r') as file_obj:
    file_content = json.load(file_obj)
print(str(file_content))
# loading the file content
data = json.loads(file_content)

salary = data["company"]["employee"]["payable"]["salary"]
print(salary)
# Access to the Employee info
employee_data = data["company"]["employee"]
print(employee_data)
# Add a new key "birth_date" to the "payable" dictionary
employee_data['birth_date']="1994-02-02"
print(employee_data)

# Convert the modified data back to JSON string
modifiedJson = json.dumps(data, indent=4)
