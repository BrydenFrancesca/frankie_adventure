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

class DeadMouse(Weapon):
    def __init__(self):
        self.name = "Dead mouse"
        self.description = """This is tasty, but also upsets humans.
        It is a good weapon"""
        self.damage = 10

class ToyOnString(Weapon):
    def __init__(self):
        self.name = "Toy on a string"
        self.description = """This bouncy toy is fun to drag around and pounce on.
        It offers maximum distraction and maximum hit points"""
        self.damage = 20

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

class Milk(Consumable):
    def __init__(self):
        self.name = "Milkie Drinks"
        self.healing_value = 30
