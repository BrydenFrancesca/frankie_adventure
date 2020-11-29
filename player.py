import items
import world
import random

class Player:
    def __init__(self):
        self.inventory = [items.Claws(), items.Dreamies(), items.ShinyRock()]

    #Add coordina0tes to player
        self.x = 2
        self.y = 2
        self.z = 0
    #Add HP to the player
        self.hp = 100
        self.mana = 5
        self.victory = False #Set winning option
        self.gold = 5

    #Give player the option to die
    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print("* " + str(item))
        print("You also have " + str(self.gold) + " gold")

    #Healing self from Inventory
    def heal(self):
        consumables = []
        for item in self.inventory:
            if isinstance(item, items.Consumable):
                consumables.append(item)
        #Print error message if no consumables
        if not consumables:
            print("You don't have any healing items")
            return
        #If do have consumables, offer options to use them
        for i, item in enumerate(consumables, 1):
            print("Choose an item to munch: ")
            print(f"{str(i)}, {item}")

        valid = False
        while not valid:
            choice = input(">")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print(f"Current HP: {str(self.hp)}")
                valid = True
            except(ValueError, IndexError):
                print("This is not nommable, try again")
                return

    #Calculation of best weapon
    def best_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    #Methods to allow the player to move
    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
        if self.mana < 10:
            self.mana += 1

    def move_north(self):
        self.move(dx = 0, dy = -1, dz = 0)

    def move_south(self):
        self.move(dx = 0, dy = 1, dz = 0)

    def move_east(self):
        self.move(dx = 1, dy = 0, dz = 0)

    def move_west(self):
        self.move(dx = -1, dy = 0, dz = 0)

    def move_up(self):
        self.move(dx = 0, dy = 0, dz = 1)

    def move_down(self):
        self.move(dx = 0, dy = 0, dz = -1)

    #Define attack on Enemy
    def attack(self):
        nice_weapon = self.best_weapon()
        room = world.tile_at(self.x, self.y, self.z)
        enemy = room.enemy
        dam = round(nice_weapon.damage * (random.random() + 0.5)) #Randomise amount of damage done
        if dam >= nice_weapon.damage:
            print("\nCRITICAL HIT!")
        print(f""" \nYou use {nice_weapon.name} against {enemy.name}!
                You did {dam} HP damage!""")
        enemy.hp -= dam

        if not enemy.is_alive():
            print(f"You killed the {enemy.name}!")
        else:
            print(f"{enemy.name} HP is {enemy.hp}")

    #Define magical attack on Enemy; destroys their HP and makes you feel better, but depleats mana
    def magic_attack(self):
        room = world.tile_at(self.x, self.y, self.z)
        enemy = room.enemy
        print(f"You use MAGIC PURR against {enemy.name}!")
        enemy.hp -= 20
        self.hp += 5
        self.mana -= 5

        if not enemy.is_alive():
            print(f"You killed the {enemy.name}!")
        else:
            print(f"{enemy.name} HP is {enemy.hp}")

    #Define Trading
    def trade(self):
        room = world.tile_at(self.x, self.y, self.z)
        room.check_if_trade(self)

    #Define talking to pupper
    def talk(self):
        room = world.tile_at(self.x, self.y, self.z)
        room.chats(self)

#Check your health
    def check_health(self):
        print(f"""
        \n You are on level {self.z}
        \n You have {self.hp} HP remaining
        You have {self.mana} mana remaining
        """)
