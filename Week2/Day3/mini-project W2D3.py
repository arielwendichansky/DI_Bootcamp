class Character:

    def __init__(self, name, life:int = 20, attack:int = 10):
        self.name = name
        self.attack = attack
        self.life = life

    def basic_attack(self,other):
        other.life -= self.attack


class Druid(Character):

    def __init__ (self, name):
        super().__init__(name)

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other: Character):
        other.life -= (0.75*self.life + 0.75*self.attack)


class Warrior(Character):

    def __init__(self, name):
        super().__init__(name)
    def brawl(self, other: Character):
        other.life -= (2*self.attack)
        self.life += (0.5*self.attack)

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self, other: Character):
        other.attack -= 3


class Mage (Character):

    def __init__(self,name):
        super().__init__(name)

    def curse(self, other: Character):
        other.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other: Character):
        other.life -= self.attack/self.life
        print (f"{other.name} life is {other.life}")


aragorn = Warrior('Aragorn')
gandalf = Mage('Gandalf')
legolas = Druid('Legolas')

aragorn.brawl(legolas)
gandalf.summon()
gandalf.cast_spell(aragorn)

