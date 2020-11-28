#General enemy class
class Enemy:
    def __init__(self):
        raise NotImplementedError ("Do not create raw enemy objects!")

    def __str__(self):
        return self.name

    #Is the enemy alive Function
    def is_alive(self):
        return self.hp > 0

#Enemies
class Hoover(Enemy):
    def __init__(self):
        self.name = "Hoover"
        self.hp = 10
        self.damage = 5
        self.prize = 2

class LooRoll(Enemy):
    def __init__(self):
        self.name = "Toilet Roll"
        self.hp = 15
        self.damage = 15
        self.prize = 3

class SprayBottle(Enemy):
    def __init__(self):
        self.name = "Spray Bottle"
        self.hp = 20
        self.damage = 10
        self.prize = 5

class LoudNoise(Enemy):
    def __init__(self):
        self.name = "LOUD NOISE"
        self.hp = 40
        self.damage = 5
        self.prize = 10

class Box(Enemy):
    def __init__(self):
        self.name = "The Box"
        self.hp = 5
        self.damage = 60
        self.prize = 30
