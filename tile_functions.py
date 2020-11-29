import random
import enemies

##Function to randomise damage
def rndm(self):
    r = random.random()
    x = int(self.enemy.damage)
    return(round(x * r))

class MapTile:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def modify_room(self, player):
        pass
        
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass
