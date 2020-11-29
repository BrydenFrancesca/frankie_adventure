import random
import enemies
import items
import npc
import tile_functions as t

##Define the various types of map t.MapTile

class StartTile(t.MapTile):
    def intro_text(self):
        return """You find yourself in a large room, full of nice soft things to snuggle on.
        It is warm here, but there is no human.
        Who will snuggle you? Unclear.
        You must find a human for optimal snug times.
        There are doors heading in four directions
        """
class KitchenTile(t.MapTile):
    def __init__(self, x, y, z):
    #Randomly generated room description
        r = random.random()
        self.been_here = False #The room knows if you have been here
        if r < 0.33:
            self.text = """
            You are in a room with a cold, shiny floor.
            There is a lot of food in here.
            For some reason, humans do not like you being in here.
            """
        elif r < 0.66:
            self.text = """
            You are in a room with a soft bed.
            There is an inadequate amount of food here, and no human.
            This is unacceptable.
            """
        else:
            self.text = """
            You are in a small room.
            There is a giant litter tray that the humans like to fill with water.
            You do not trust the giant litter tray
            """
        super().__init__(x,y,z)

    def intro_text(self):
        if not self.been_here:
            self.been_here = True #The room knows if you have been here
            return self.text
        else:
            return self.text + "\n It smells like you have been here before \n"

class StairsTile(t.MapTile):
    def __init__(self, x, y, z):
        self.text = """
        You are in the mighty hill room.
        A hill of steps stretches upward. The way is blocked by a large box.
        Another stretches downwards into a deep, spooky cellar.
        You would like to climb both up and down. """

        super().__init__(x,y,z)
    def intro_text(self):
        return self.text


class TraderTile(t.MapTile):
    def __init__(self, x, y, z):
        self.trader = npc.Trader()
        super().__init__(x, y, z)

    #Trading Function
    def trade(self, buyer, seller, player):
        while True:
            for i, item in enumerate(seller.inventory, 1):
                print(f"{i}. {item.name} - {item.value}")
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ["Q", "q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap, player)
                except ValueError:
                    print("Invalid choice!")

    #Define swapping Function
    def swap(self, seller, buyer, item, player):
        if item.value > buyer.gold:
            print("That's too expensive!")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print(f"Trade complete! You have {player.gold} gold now")

    #Function to initate trade
    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                print("The bunny opens his backpack to reveal the following: ")
                self.trade(buyer = player, seller = self.trader, player = player)
            elif user_input in ["S", "s"]:
                print("You check what you have in your inventory to sell: ")
                self.trade(buyer = self.trader, seller = player, player = player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        You are in a large room that is all made of windows.
        There is a very floofy bunny here.
        He looks like he might be willing to trade with you.
        """


class OutsideTile(t.MapTile):
    def __init__(self, x, y, z):
    #Randomly generated enemy tile
        r = random.random()
        if r < 0.2:
            self.item = items.Dreamies()
        elif r < 0.4:
            self.item = items.DeadMouse()
        elif r < 0.6:
            self.item = items.Carrot()
        elif r < 0.8:
            self.item = items.Milk()
        else:
            self.item = items.ToyOnString()

        self.claimed = False
        super().__init__(x,y,z)

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

class BallTile(t.MapTile):
    def __init__(self, x, y, z):
        self.item = items.Ball()
        self.claimed = False
        super().__init__(x,y,z)

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


class EnemyTile(t.MapTile):
    def __init__(self, x, y, z):
        self.claimed = False #Gold has not been claimed yet
        self.been_here = False #The room knows if you have been here
    #Randomly generated enemy tile
        r = random.random()
        if r < 0.3:
            self.enemy = enemies.Hoover()
            self.alive_text = "A fearsome Hoover blocks your path!"
            self.dead_text = f"""The slain corpse of the Hoover lies on the floor.
            It has dropped {self.enemy.prize} pieces of gold"""
            self.taken_prize = "The slain corpse of the Hoover lies on the floor."
        elif r < 0.6:
            self.enemy = enemies.LooRoll()
            self.alive_text = "A chonky loo roll lies in your path menacingly!"
            self.dead_text = f"""You have shredded the loo roll into tiny chunks.
            It has dropped {self.enemy.prize} pieces of gold"""
            self.taken_prize = "You step over a shredded loo roll. May you should chew it some more?"
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

        super().__init__(x,y,z)
    #Generate intro text
    def intro_text(self):
        if self.enemy.is_alive():
            return(self.alive_text)
        elif self.claimed == False:
            return(self.dead_text)
        elif self.been_here == False:
            self.been_here = True
            return(self.taken_prize)
        else:
            return(self.taken_prize + ". \nIt smells like you have been here before.")


    #Make the enemy attack
    def modify_player(self, player):
        if self.enemy.is_alive():
            dam = t.rndm(self)
            player.hp -= dam
            if dam == self.enemy.damage:
                print("CRITICAL HIT!!")
            print(f"""You have taken {dam} damage!
            You have {player.hp} health remaining""")
    #Pick up the item
        elif self.claimed == False:
            self.claimed = True
            player.gold = player.gold + self.enemy.prize

class BossTile(t.MapTile):
    def __init__(self, x, y, z):
        self.claimed = False #Gold has not been claimed yet
        self.been_here = False #The room knows if you have been here
    #Randomly generated enemy tile
        self.enemy = enemies.BoxBoss()
        self.alive_text = "OH NO IT IS THE BOX! It has returned, larger and angrier than ever!"
        self.dead_text = f"""The mighty defeated Box lies at your feet.
        It has dropped {self.enemy.prize} pieces of gold"""
        self.taken_prize = "Once again, you step over the corpse of the defeated Box."

        super().__init__(x,y,z)
    #Generate intro text
    def intro_text(self):
        if self.enemy.is_alive():
            return(self.alive_text)
        elif self.claimed == False:
            return(self.dead_text)
        elif self.been_here == False:
            self.been_here = True
            return(self.taken_prize)
        else:
            return(self.taken_prize + ". \nIt smells like you have been here before.")

    #Make the enemy attack
    def modify_player(self, player):
        if self.enemy.is_alive():
            dam = t.rndm(self)
            player.hp -= dam
            if dam == self.enemy.damage:
                print("CRITICAL HIT!!")
            print(f"""You have taken {dam} damage!
            You have {player.hp} health remaining""")
    #Pick up the item
        elif self.claimed == False:
            self.claimed = True
            player.gold = player.gold + self.enemy.prize



class VictoryTile(t.MapTile):
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
