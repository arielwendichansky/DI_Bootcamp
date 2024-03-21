#  Exercise 1 : Pets
# Instructions
# Using this code:
#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.
#
#
# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
#
# Create 3 dogs and run them through your class.
#
#
# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
#
# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
#
# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
#
#
# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:
#
# members: list of dictionaries
# last_name : (string)
#
# Implement the following methods:
#
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.
#
# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.
#
#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]
#
#
# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
#
#
# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
#
#
# Add a method called incredible_presentation which :
#
# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
#
#
# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
#
#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]
# Call the incredible_presentation method.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Call the incredible_presentation method again.

#Exrcise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [Bengal('Pablo',1),Chartreux('Neymar',10),Siamese('Ronaldinhio',1)]

sara_pets = Pets(all_cats)
sara_pets.walk()

print('*'*30)
#Exrcise 2

class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        run_speed = int(self.weight/self.age*10)
        print(f"{self.name} can run at a speed of {run_speed} ")
        return run_speed


    def fight(self,other_dog):
        dogs_fight = self.run_speed() * self.weight
        other_dog_compare = int(other_dog.run_speed() * other_dog.weight)
        if dogs_fight > other_dog_compare:
            print(f"{self.name} is stronger than {other_dog.name}")
        elif dogs_fight == other_dog_compare:
            print("Both dogs are equally strong")
        else:
            print(f"{self.name} is weaker than {other_dog.name}")

dog1 = Dog('Shemesh',3,9)
dog2 = Dog('Bethoven',4,14)
dog3 = Dog('Pure',7,5)
dog1.bark()
dog2.run_speed()
dog1.fight(dog3)


print('*'*30)
#Exrcise 4

class Family:
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = []

    def exiting_members(self,**kwargs):
        self.members.append(kwargs)
    def born(self,**kwargs):
        self.members.append(kwargs)
        print("Congratulations for the new member")

    def is_18(self):
        ages = [sub['age']for sub in self.members]
        member_age= ages[0]
        if member_age > 18:
            return print(True)
        else:
            return print(False)

    def family_presentation(self):
        print(f"Here a is a member from the family {self.last_name}")
        print(f"some info about it {self.members}")

Michael = Family("Perez")
Michael.exiting_members(name='Michael',age=35,gender='Male',is_child=False)
Michael.is_18()
Michael.family_presentation()
Sarah = Family("Leon")
Sarah.exiting_members(name='Sarah',age=32,gender='Female',is_child=False)
Sarah.is_18()
Sarah.family_presentation()

print('*'*30)
#Exrcise 5

class TheIncredibles(Family):
    def __init__(self,last_name,):
        super().__init__(last_name)

    def use_power(self):
        try:
            if self.is_18():
                print(f"You can use the power {self.power}")
                raise Exception ('You are too young to use your power')
        except Exception as e:
            print(e)

    def incredible_presentation(self):
        print("Here is our powerful family")
        print(f"{self.last_name}")
        print(f"Some details about our family members {self.members}")

Los_Increibles = TheIncredibles("Los Increibles")
Los_Increibles.exiting_members(name='Michael',age= 35,gender='Male',is_child= False, power='fly',incredible_name='MikeFly')
Los_Increibles.exiting_members( name='Sarah',age=32,gender='Female',is_child=False,power='read minds',incredible_name='SuperWoman')
Los_Increibles.born( name='Jack',age=0,gender='Male',is_child=True,power='unknown',incredible_name='Jackjack')
Los_Increibles.incredible_presentation()






