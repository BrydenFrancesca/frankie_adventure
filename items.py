##Create overall weapon class----------
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw weapon objects")
    def __str__(self):
        return self.name + ". Damage: " + str(self.damage)

#Create individual weapon classes----------
class Claws(Weapon):
    def __init__(self):
        self.name = "Claws"
        self.description = """You are smol, but your claws are sharp.
        You can do damage with these"""
        self.damage = 5
        self.value = 0

class DeadMouse(Weapon):
    def __init__(self):
        self.name = "Dead mouse"
        self.description = """This is tasty, but also upsets humans.
        It is a good weapon"""
        self.damage = 10
        self.value = 5

class ToyOnString(Weapon):
    def __init__(self):
        self.name = "Toy on a string"
        self.description = """This bouncy toy is fun to drag around and pounce on.
        It offers maximum distraction and maximum hit points"""
        self.damage = 20
        self.value = 10

class MetalClaws(Weapon):
    def __init__(self):
        self.name = "Titanium Coated Claws"
        self.description = """These titanium-coated claws are shiny AND strong.
        Enemies will cower before you"""
        self.damage = 50
        self.value = 50

#Create overall consumables class
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw consumables objects")
    def __str__(self):
        return self.name + "(" + str(self.healing_value) + "HP)"

class Dreamies(Consumable):
    def __init__(self):
        self.name = "Dreamies"
        self.healing_value = 10
        self.value = 10

class Carrot(Consumable):
    def __init__(self):
        self.name = "Carrot"
        self.healing_value = 2
        self.value = 40

class Milk(Consumable):
    def __init__(self):
        self.name = "Milkie Drinks"
        self.healing_value = 30
        self.value = 20

class HumanFood(Consumable):
    def __init__(self):
        self.name = "Human food (nomnom)"
        self.healing_value = 50
        self.value = 30

##Create overall quest and useful item class----------
class Questable:
    def __init__(self):
        raise NotImplementedError("Do not create raw weapon objects")
    def __str__(self):
        return self.name + ". " + str(self.description)

class ShinyRock(Questable):
    def __init__(self):
        self.name = "Shiny rock"
        self.description = """This rock glows with an unusual light.
        It is good at lighting up dark spaces"""
        self.value = 0

class Ball(Questable):
    def __init__(self):
        self.name = "Bouncy ball"
        self.description = """This bouncy ball looks like it would be fun to play with"""
        self.value = 1000

class Keys(Questable):
    def __init__(self):
        self.name = "Keys"
        self.description = """I think these are important"""
        self.value = 1000
