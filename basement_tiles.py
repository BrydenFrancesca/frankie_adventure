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
            return "You are in a dingy basement room"
        else:
            return """\n This room is the darkest dark cave.
            Even you, with your superior kitten eyes cannot see.
            There are probably spiders and stuff.
            You don't want to go any further without a light.
            """

class WizardTile(t.MapTile):
    def __init__(self, x, y, z):
        self.wizard = npc.Doggo()
        self.been_here = False #The room knows if you have been here
        self.claimed = False
        self.item = items.ShinyRock()
        super().__init__(x, y, z)

    #Trading Function
    def chats(self, player):
        while True:
            print("Would you like to: ")
            print("(H)iss at the pupper")
            if self.been_here == False: #If you haven't been here before
                print("(B)op him on the nose?")
            for item in player.inventory: #Option to go into dark places
                if isinstance(item, items.Ball):
                    print("(T)hrow the ball?")
            print("(Q)uit")
            user_input = input()
            if user_input in ["H", "h"]:
                print("The doggo cries. You are smug")
                return
            elif user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                player.hp = 120
                print(f"""The pupper is heckin pleased.
                You also feel good, for some reason.
                Your HP is now {player.hp}""")
                self.been_here = True
                return
            elif user_input in ["T", "t"]:
                player.hp = 120
                print(f"""The pupper is HECKIN pleased.
                He loves the ball.
                He would like you to have something in return.
                He gives you a shiny rock.""")
                if not self.claimed:
                    self.claimed = True
                    player.inventory.append(self.item) #Removing ball from inventory
                    for i, o in enumerate(player.inventory):
                        if o.name == "Bouncy ball":
                            del player.inventory[i]
                            break
                return
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        You are in the out. It smells like doggo here.
        A heckin pupper licks your nose.
        """

class HumanTile(t.MapTile):
    def __init__(self, x, y, z):
        self.been_here = False #The room knows if you have been here
        self.claimed = False
        super().__init__(x, y, z)

    #Trading Function
    def chats(self, player):
        while True:
            print("Would you like to: ")
            print("(H)iss at the pupper")
            if self.been_here == False: #If you haven't been here before
                print("(B)op him on the nose?")
            for item in player.inventory: #Option to go into dark places
                if isinstance(item, items.Ball):
                    print("(T)hrow the ball?")
            print("(Q)uit")
            user_input = input()
            if user_input in ["H", "h"]:
                print("The doggo cries. You are smug")
                return
            elif user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                player.hp = 120
                print(f"""The pupper is heckin pleased.
                You also feel good, for some reason.
                Your HP is now {player.hp}""")
                self.been_here = True
                return
            elif user_input in ["T", "t"]:
                player.hp = 120
                print(f"""The pupper is HECKIN pleased.
                He loves the ball.
                He would like you to have something in return.
                He gives you a shiny rock.""")
                if not self.claimed:
                    self.claimed = True
                    player.inventory.append(self.item) #Removing ball from inventory
                    for i, o in enumerate(player.inventory):
                        if o.name == "Bouncy ball":
                            del player.inventory[i]
                            break
                return
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        You are in the out. It smells like doggo here.
        A heckin pupper licks your nose.
        """
