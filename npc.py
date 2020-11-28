import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects!")

    def __str__(self):
        return self.name


class Doggo(NonPlayableCharacter):
    def __init__(self):
        self.name = "Heckin Doggo"

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Floofy Bun"
        self.gold = 100
        self.inventory = [items.Dreamies(), items.MetalClaws(), items.Dreamies(), items.DeadMouse(), items.HumanFood()]
