from player import Player
from collections import OrderedDict
import world
import enemies
import tile_descriptions as td

#Make it so only appropriate actions are available
def get_available_actions(room, player):
    actions = OrderedDict()
    print("\nChoose an action: ")
    action_adder(actions, "k", player.check_health, "Check health")
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Print inventory")
    if isinstance(room, td.StairsTile): #Add climb stairs option when in stairs room
        action_adder(actions, "u", player.climb, "Go Upstairs")
    if isinstance(room, td.TraderTile):
        action_adder(actions, "t", player.trade, "Trade")
    if isinstance(room, td.WizardTile) and room.been_here == False:
        action_adder(actions, "c", player.talk, "Talk")
    if isinstance(room, td.EnemyTile) or isinstance(room, td.BossTile):
        if room.enemy.is_alive():
            action_adder(actions, "a", player.attack, "Attack")
            if player.mana > 5:
                action_adder(actions, "p", player.magic_attack, "Magic Purr Attack")
        elif not room.enemy.is_alive():
            if world.tile_at(room.x, room.y - 1):
                action_adder(actions, "n", player.move_north, "Go north")
            if world.tile_at(room.x, room.y + 1):
                action_adder(actions, "s", player.move_south, "Go south")
            if world.tile_at(room.x + 1, room.y):
                action_adder(actions, "e", player.move_east, "Go east")
            if world.tile_at(room.x - 1, room.y):
                action_adder(actions, "w", player.move_west, "Go west")
    else:
    #Move in normal tiles
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, "n", player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, "s", player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, "e", player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, "w", player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, "h", player.heal, "Heal")

    return actions

#Define action adding
def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

#Use dictionary to get available options
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")

#Game loop
def play():
    print("Welcome to the Frankie Adventure!")
    world.parse_world_dsl()
    #Initialise player environment here
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player) #Allow enemies to attack
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("""You tire of this nonsense.
            You hide under the sideboard and refuse to play any more...""")

play()
