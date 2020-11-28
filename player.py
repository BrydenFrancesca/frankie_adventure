import items
import world

class Player:
    def __init__(self):
        self.inventory = [items.Claws(), items.Dreamies()]

    #Add coordinates to player
        self.x = 1
        self.y = 2
    #Add HP to the player
        self.hp = 100
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
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx = 0, dy = -1)

    def move_south(self):
        self.move(dx = 0, dy = 1)

    def move_east(self):
        self.move(dx = 1, dy = 0)

    def move_west(self):
        self.move(dx = -1, dy = 0)

    #Define attack on Enemy
    def attack(self):
        nice_weapon = self.best_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print(f"You use {nice_weapon.name} against {enemy.name}!")
        enemy.hp -= nice_weapon.damage

        if not enemy.is_alive():
            print(f"You killed the {enemy.name}!")
        else:
            print(f"{enemy.name} HP is {enemy.hp}")
