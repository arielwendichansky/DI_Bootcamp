from Exercise_XP_W2D2 import Dog
import random

class PetDog (Dog):
    def __init__(self,name,age,weight,trained=False):
        super().__init__(name,age,weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self,*args):
        dog_names = ','.join(args)
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained == True:
            tricks=["does a barrel roll","stands on his back legs","shakes your hand", "plays dead"]
            random_trick = random.choice(tricks)
            print(f"{self.name} {random_trick}")
        else:
            print(f"{self.name} is not a trained dog")

dog1 = PetDog('Shemesh',3,9,)
dog2 = PetDog('Bethoven',4,14)
dog3 = PetDog('Pure',7,5)

dog1.train()
dog1.do_a_trick()
dog2.play("Shemes","a","b")

