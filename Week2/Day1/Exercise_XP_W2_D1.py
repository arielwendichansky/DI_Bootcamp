# Using this class
#
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
#Exercise1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def say_hi(self):
        print(f"Owner: {self.name} say Hi!")
        print(f"{self.name}: Miau!")
    def walk(self,walk_meters):
        self.walk_meters = walk_meters
        print(f"{self.name} walked {self.walk_meters} meters")

    def toy(self, toy):
        self.toy = toy
        print(f"{self.name} favorite toy is  {toy}")

first_cat = Cat("Kitty", 5)
first_cat.say_hi()
first_cat.walk(50)
first_cat.toy("ball")
second_cat = Cat("Pablo", 4)
third_cat = Cat("Julio", 7)

cats = [first_cat, second_cat, third_cat]
def oldest_cat ():
    cats_names = [cat.name for cat in cats]
    cats_ages = [cat.age for cat in cats]

    old_cat = max(cats_ages)
    oldest_reference = cats_ages.index(old_cat)
    oldest_name = cats_names[oldest_reference]
    print(f"The oldest cat is {oldest_name}, and is {old_cat} years old.")

oldest_cat()

#Exercise2
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = int(height)

    def bark (self):
        print(f" {self.name} goes woof!")

    def jump (self):
        print(f" {self.name} jumps {self.height*2}!")

davids_dog = Dog("Rex",50)
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog ("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

dogs = [davids_dog,sarahs_dog]
dog_height = [dog.height for dog in dogs]
dog_name = [dog.name for dog in dogs]
bigger_dog = max(dog_height)
bigger_index = dog_height.index(bigger_dog)
highest_name = dog_name [bigger_index]
print(f"The biggest dog is {highest_name}.")

#Exercise 3
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
#
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#
#
# Then, call the sing_me_a_song method. The output should be:
#
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__ (self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyrics in self.lyrics:
            print(lyrics)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#Exercise4
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

class Zoo:
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        self.animals.append(new_animal)
        self.animals = list(set(self.animals))

    def get_animals(self):
        print(self.animals)
    def sell_animals(self,animal_sold):

        self.animals.remove(animal_sold)
        print(self.animals)

    def sort_animals(self):
        self.animals = sorted(self.animals)
        list_animal = []
        x = []
        for i in self.animals:
            if i[0] not in x:
                x.append(i[0])
        for i in x:
            p = []
            for j in self.animals:
                if j[0] == i:
                    p.append(j)
            list_animal.append(p)
        dic_animals = {index + 1: animals for index, animals in enumerate(list_animal)}
        self.animals = dic_animals
        print(self.animals)

    def get_group(self):
        print(self.animals)


ramat_gan_safari = Zoo("Ramat Gan")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.sell_animals("Bear")
ramat_gan_safari.sort_animals()


