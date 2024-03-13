import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path+'\\nameslist.txt')
#imported file
with open (dir_path+'\\nameslist.txt','r') as file_obj:
    content = file_obj.readlines()
    #reading the file line by line
    for line in open('nameslist.txt'):
        print(line)
    #reading only the 5th line
    print(content[5:6])
    file_obj.seek(0)
    content1 = file_obj.read(5)
    print(content1)
    #Taking every line as a list and taking out the trailing between them
    contents = [item.rstrip('\n') for item in content]
    string_content = ", ".join(contents)
    #create a String with every line
    print(string_content)
    # Counting how many times does these names are repeated
    file_obj.seek(0)
    darth_counter = 0
    luke_counter = 0
    lea_counter = 0
    for i in content:
        if i.lower().strip('\n') == 'darth':
            darth_counter +=1
        elif i.lower().strip('\n') == 'luke':
            luke_counter +=1
        elif i.lower().strip('\n') == 'lea':
            lea_counter +=1
    print(f"There are Darth {darth_counter}, there are Luke {luke_counter}, there are Lea {lea_counter}")

#Appending my name to the bottom of the list
with open(dir_path + '\\nameslist.txt', 'a+') as file_obj:
    my_name = file_obj.write("Wendichansky Ariel")
    print(content)

#Writing all over the list from the top and appending Sywalker to Luke
with open(dir_path + '\\nameslist.txt', 'w') as file_obj:
    file_obj.seek(0) #start from the top
    for item in range(len(content)):
        content[item] = content[item].rstrip('\n')  # Remove trailing newline character
        if content[item] == 'Luke':
            content[item] += " SkyWalker"
        content[item] +='\n' # adding back the trailing newline character
        file_obj.write(content[item])
    print(content)


