class Character():
    _name = "Random Guy"
    # Dunder method
    def __init__(self, name, age):
        # private variable convention
        self._name = name
        self._age = age
    
    def shout(self, msg):
        print(f"{self._name}: {msg}")
    
    # Dunder method
    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"
    
    '''
        - @classmethod: can be called without create an object of the class, also can access to global class variable
        - @staticmethod: can be called without create an object of the class, but can't access to global class variable
    '''
    @classmethod
    def background_action(cls, action_name):
        return f'{cls._name} {action_name}.'
    
    @classmethod
    def attack(cls):
        print(f"{cls._name} make an attack with a normal punch")
    
    @staticmethod
    def narrative():
        return 'Wano country, on the night of fire festival ...\n'

class Hero(Character):
    def __init__(self, name, age):
        super().__init__(name, age)

    def help(self):
        print(f'{self._name} is fighting for Wano!')
    
    def attack(self, attack_name):
        print(f"{self._name} make an attack with {attack_name}")

class Villain(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def cause_trouble(self):
        print(f'{self._name} is destroying Wano!')
    
    def attack(self, attack_name):
        print(f"{self._name} make an attack with {attack_name}")

class AntiHero(Hero, Villain):
    pass

print(Character.narrative())
character1 = Hero('Luffy', 19)
character2 = Hero('Zoro', 21)
character3 = Villain('Kaido', 59)
character4 = AntiHero('Kidd', 28)

print(str(character1))
character1.help()
character1.attack('Gomu Gomu no Red Hoc')
character1.shout("I'm going to be The Pirate King!\n")

print(str(character2))
character2.help()
character2.attack('Three sword style: Dragon Twister')
character2.shout("Nothing Happened!\n")

print(str(character3))
character3.cause_trouble()
character3.attack('Thunder Baugua')
character3.shout("All of you are not Joyboy!\n")

print(str(character4))
character4.cause_trouble()
character4.help()
character4.attack('Punk Rotten')
character4.shout("I'm the one who behead Kaido\n")

print(Character.background_action('are Enjoying the festival'))
Character.attack()