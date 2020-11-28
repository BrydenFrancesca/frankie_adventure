import random
import enemies
import items

###Abbreviated map
world_dsl = """
| |OT|ET|ET|OT|
|OT|ET| |VT|ET|
|KT|ST|OT|ET| |
| |ET|KT|ET| |
| |OT| |OT|ET|
"""

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
            You pick up {self.item} here.
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
    #Randomly generated enemy tile
        r = random.random()
        if r < 0.4:
            self.enemy = enemies.Hoover()
            self.alive_text = "A fearsome Hoover blocks your path!"
            self.dead_text = "The slain corpse of the Hoover lies on the floor"
        elif r < 0.8:
            self.enemy = enemies.SprayBottle()
            self.alive_text = "A cunning Spray Bottle full of water attacks you!"
            self.dead_text = "The defeated Spray Bottle is in pieces on the floor"
        elif r < 0.9:
            self.enemy = enemies.LoudNoise()
            self.alive_text = "There is a Loud Noise hiding here!"
            self.dead_text = "You have vanquished the Loud Noise that once lived here"
        else:
            self.enemy = enemies.Box()
            self.alive_text = "IT IS THE BOX! WE DO NOT LIKE THE BOX!"
            self.dead_text = "You step over the corpse of the mighty Box which you defeated"

        super().__init__(x,y)
    #Generate intro text
    def intro_text(self):
        if self.enemy.is_alive():
            return(self.alive_text)
        else:
            return(self.dead_text)

    #Make the enemy attack
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp -= self.enemy.damage
            print(f"""You have taken {self.enemy.damage} damage!
            You have {player.hp} health remaining""")

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
