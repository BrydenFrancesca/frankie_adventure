import random
import enemies
import items
import npc

###Abbreviated map
world_dsl = """
| |OT|ET|ET|OT|
|OT|ET| |VT|ET|
|KT|ST|OT|TT| |
| |ET|KT|ET| |
| |OT| |OT|ET|
"""

##Function to randomise damage
def rndm(self):
    r = random.random()
    x = int(self.enemy.damage)
    return(round(x * r))

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

##Define the various types of map MapTile

class StartTile(MapTile):
    def intro_text(self):
        return """You find yourself in a large room, full of nice soft things to snuggle on.
        It is warm here, but there is no human.
        Who will snuggle you? Unclear.
        You must find a human for optimal snug times.
        There are doors heading in four directions
        """
class KitchenTile(MapTile):
    def intro_text(self):
        return """
        You are in a room with a cold, shiny floor.
        There is a lot of food in here.
        For some reason, humans do not like you being in here.
        """

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    #Trading Function
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print(f"{i}. {item.name} - {item.value})
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ["Q", "q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    #Define swapping Function
    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive!")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    #Function to initate trade
    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                print("The bunny opens his backpack to reveal the following: ")
                self.trade(buyer = player, seller = self.trader)
            elif user_input in ["S", "s"]:
                print("You check what you have in your inventory to sell: ")
                self.trade(buyer = self.trader, seller = player)
            else:
                print("Invalid choice!")    

    def intro_text(self):
        return """
        You are in a large room that is all made of windows.
        There is a very floofy bunny here.
        He looks like he might be willing to trade with you.
        """


class OutsideTile(MapTile):
    def __init__(self, x, y):
    #Randomly generated enemy tile
        r = random.random()
        if r < 0.4:
            self.item = items.Dreamies()
        elif r < 0.6:
            self.item = items.DeadMouse()
        elif r < 0.8:
            self.item = items.Milk()
        else:
            self.item = items.ToyOnString()

        self.claimed = False
        super().__init__(x,y)

    def intro_text(self):
        if not self.claimed:
            return f"""
            You are in the out.
            Sometimes water falls from the sky when you are here.
            This is not optimal.
            Snuffling on the floor, you find a {self.item}.
            """
        else:
            return f"""
            You are in the out.
            It smells like you have already been here before
            """
#Pick up the item
    def modify_player(self, player):
        if not self.claimed:
            self.claimed = True
            player.inventory.append(self.item)



class EnemyTile(MapTile):
    def __init__(self, x, y):
        self.claimed = False #Gold has not been claimed yet
        self.been_here = False #The room knows if you have been here
    #Randomly generated enemy tile
        r = random.random()
        if r < 0.4:
            self.enemy = enemies.Hoover()
            self.alive_text = "A fearsome Hoover blocks your path!"
            self.dead_text = f"""The slain corpse of the Hoover lies on the floor.
            It has dropped {self.enemy.prize} pieces of gold"""
            self.taken_prize = "The slain corpse of the Hoover lies on the floor."
        elif r < 0.8:
            self.enemy = enemies.SprayBottle()
            self.alive_text = "A cunning Spray Bottle full of water attacks you!"
            self.dead_text = f"""The defeated Spray Bottle is in pieces on the floor. .
            It has dropped {self.enemy.prize} pieces of gold"""
            self.taken_prize = "The defeated Spray Bottle is in pieces on the floor"
        elif r < 0.9:
            self.enemy = enemies.LoudNoise()
            self.alive_text = "There is a Loud Noise hiding here!"
            self.dead_text = f"""You have vanquished the Loud Noise that once lived here.
            It has dropped {self.enemy.prize} pieces of gold"""
            self.taken_prize = "This room is empty and very quiet"
        else:
            self.enemy = enemies.Box()
            self.alive_text = "IT IS THE BOX! WE DO NOT LIKE THE BOX!"
            self.dead_text = f"""You step over the corpse of the mighty Box which you defeated.
            It has dropped {self.enemy.prize} pieces of gold"""
            self.taken_prize = "You step over the corpse of the mighty Box which you defeated"

        super().__init__(x,y)
    #Generate intro text
    def intro_text(self):
        if self.enemy.is_alive():
            return(self.alive_text)
        elif self.claimed == False:
            return(self.dead_text)
        elif self.been_here == False:
            self.been_here = True
            return(self.taken_prize + ". \nIt smells like you have been here before.")

    #Make the enemy attack
    def modify_player(self, player):
        if self.enemy.is_alive():
            dam = rndm(self)
            player.hp -= dam
            if dam == self.enemy.damage:
                print("CRITICAL HIT!!")
            print(f"""You have taken {dam} damage!
            You have {player.hp} health remaining""")
    #Pick up the item
        elif self.claimed == False:
            self.claimed = True
            player.gold = player.gold + self.enemy.prize

class VictoryTile(MapTile):
    #Set value to win
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You have arrived in a warm, soft room.
        It has a wide bed, and a soft human asleep on that bed.
        You can tell that the human would like your paw on his face.
        Possibly he will stroke you in return.
        This will be a good day...
        """

##Locate tile at a coordinate
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

#Dictionary of tile types
tile_type_dict =  {"VT": VictoryTile,
                   "ET": EnemyTile,
                   "ST": StartTile,
                   "KT": KitchenTile,
                   "OT": OutsideTile,
                   "TT": TraderTile,
                   " ": None}

##Layout the grid of the map
world_map = []

#Define automated map function
def parse_world_dsl():
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else None)
        world_map.append(row)
