# Exercise 1
# What is a class?
# A class in Python is like a blueprint for creating objects. It helps organize code in a way that makes it easier
# to work with related pieces of information and functionality.

# What is an instance?
# An instance in Python is simply a specific object created using a class blueprint. You can create many instances
# of the same class, each with its own unique characteristics.

# What is encapsulation?
# Encapsulation is a concept in programming that involves bundling data and the methods that operate on that data
# together within a single unit, typically a class. It's used to protect the data inside from being modified by
# outside code. You can set rules and conditions for accessing and modifying the data.

# What is abstraction?
# It hides the internal implementation details of a class from the outside world, providing a clear and simplified
# interface for interacting with the class. Users of the class only need to know how to use its methods,
# not how they are implemented.

# What is inheritance?
# Inheritance allows you to create a hierarchy of classes, with each subclass specializing
# and extending the behavior of its superclass.
# This promotes code reuse, improves readability, and makes it easier to maintain and extend your codebase.

# What is multiple inheritance?
# Is when a subclass can inherit properties and behavior from multiple parent classes.
# This means that a class can have more than one direct superclass.

# What is polymorphism?
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# It enables a single interface to represent different types of objects,
# providing flexibility and extensibility in the code.

# What is method resolution order or MRO?
# Is the order in which methods are searched for and executed in classes that utilize multiple inheritance.
# It defines the sequence in which the base classes are traversed
# when looking for a method or attribute in a class hierarchy.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
#
# The requirements are as follows:
#
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck.
# After a card is dealt, it should be removed from the deck.

import random


class Card:
    def __init__(self):
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck_cards = self.deck_cards_creation()

     #using static method as I don't need to make any changes in the attributes from the class, nor depend on it.
    @staticmethod
    def deck_cards_creation():
        # Create a tuple inside the list, so I don't have repeated cards.
        return [(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]


class Deck:
    def __init__(self):
        self.deck_of_cards = Card().deck_cards  # Initialize deck_of_cards using Card's deck_cards_creation
        self.shuffled = False

    def shuffle(self):
        if len(self.deck_of_cards) != 52:
            print("There are cards missing  in the deck")
        else:
            random.shuffle(self.deck_of_cards)
            self.shuffled = True

    def deal(self):
        cards_out = []
        while True:
            print("You want a card or to stay? \n"
                  ">>> 1 - I want one\n"
                  ">>> 2 - I stay")
            valid_ans = (1, 2)
            ans = int(input(">>> "))
            if ans not in valid_ans:
                print("You have input an invalid character, only 1 and 2 is accepted")
                ans = int(input(">>> "))
            elif ans == 1:
                if not self.shuffled:  # check if the deal has been shuffled
                    self.shuffle()
                dealt_card = self.deck_of_cards.pop(0)  # Allways taking the 1st card as it has been shuffled before.
                print(f"Dealt card: {dealt_card[1]} of {dealt_card[0]}")
                cards_out.append(dealt_card)
            elif ans == 2:
                print(f"Thanks for playing, these are your cards:\n{cards_out}")
                cards_out = []
                self.deck_of_cards = Card().deck_cards
                break


test1 = Deck()
test1.deal()

