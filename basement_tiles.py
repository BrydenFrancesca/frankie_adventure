import random
import enemies
import items
import npc
import player
import tile_functions as t


class BasementTile(t.MapTile):
    #Set value to win
    def modify_room(self, player):
        for item in player.inventory: #Option to go into dark places
            if isinstance(item, items.ShinyRock):
                self.light = True
            else:
                self.light = False

    def intro_text(self):
        if self.light == True:
            return "Light"
        else:
            return "Dark"
