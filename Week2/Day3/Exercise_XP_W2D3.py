#Exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE
    #@staticmethod
    def __str__(self):
        output = f'''{self.amount} {self.currency}'''
        return output

    @staticmethod
    def __int__(amount):
        return amount

    def __repr__(self):
        output2 = f'''{self.amount} {self.currency}'''
        return output2

    def __add__(self,other):
        try:
            if isinstance(other,Currency):
                if other.currency == self.currency:
                    return (other.amount+self.amount)
                else:
                    raise ValueError("Cannot add between Currency type dollar and shekel")
            else:
                return self.amount + other
        except ValueError as e:
            print(e)

    def __iadd__(self,other):
        try:
            if isinstance(other,Currency):
                if other.currency == self.currency:
                    print("before adding")
                    self.amount+=other.amount
                else:
                    raise ValueError("Cannot add between Currency type dollar and shekel")
            else:
                self.amount += other
            return self
        except ValueError as e:
            print(e)



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
#print(c1.__str__('dollar', 5))
print(c1)
print(c1.__int__(5)) #using @staticmethod
print(repr(c1))
print(c1+5)
print("---")
print(c1+c2)
print("---")
print(c1)
print("---")
c1+=5
print(c1)
print("---")
c1 += c2
print(c1)
print(c1 + c3)

# Exercise 3
import string
import random


def random_word (lenght=5):
    random_list_letter = string.ascii_letters
    random_string = "".join(random.choice(random_list_letter)for i in range(lenght))

    return print(random_string)
random_word()

# Exercise 4
from datetime import date
def day():
    today = date.today()
    print(today)

day()

# Exercise 5
from datetime import datetime,timedelta

def time_difference():
    today = datetime.now()
    future_date = datetime(2025,1,10,10,34,1)
    timedelta = future_date - today
    print(f"is missing {timedelta} hours to arrive to this date")

time_difference()

# Exercise 6

def birthday_input(birthday):
    time_lived = datetime.now()-birthday
    print(f"You have lived {time_lived} hours so far")

# date_str = input("When is you where born (yyyy-mm-dd)?")
# birthday_date = datetime.strptime(date_str, "%Y-%m-%d")
# birthday_input(birthday_date)

# Exercise 7
from faker import Faker

fake = Faker()
users =[]
def fake_list():
    user={ 'name': fake.name(),
            'address':fake.address(),
            'language_code':fake.language_code()
            }
    return user
user1=fake_list()
users.append(user1)
user2=fake_list()
users.append(user2)
user3=fake_list()
users.append(user3)
print(users)