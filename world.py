import random
import enemies
import items
import npc
import tile_descriptions as td

###Abbreviated map
world_down = """
|  |OT|ET|ET|OT|
|WT|  |ET|KT|ET|
|KT|OT|ST|ET|KT|
|ET|KT|KT|ET|TT|
|  |OT|UT|OT|ET|

"""

world_up = """
|  |OT|ET|ET|OT|
|WT|  |ET|KT|ET|
|KT|OT|ST|ET|KT|
|ET|KT|KT|ET|  |
|  |KT|OT|KT|ET|

"""


##Locate tile at a coordinate
def tile_at(x, y, z):
    if x < 0 or y < 0 or z < 0:
        return None
    try:
        return world_map[z][y][x]
    except IndexError:
        return None

#Dictionary of tile types
tile_type_dict =  {"VT": td.VictoryTile,
                   "ET": td.EnemyTile,
                   "ST": td.StartTile,
                   "KT": td.KitchenTile,
                   "OT": td.OutsideTile,
                   "TT": td.TraderTile,
                   "WT": td.WizardTile,
                   "BT": td.BossTile,
                   "UT": td.StairsTile,
                   "  ": None}

##Layout the grid of the map
world_map = []

#Define automated map function
def parse_world_dsl():
    z = 0
    for ta in [world_down, world_up]:
        table = []
        dsl_lines = ta.splitlines()
        dsl_lines = [x for x in dsl_lines if x]
        z += 1

        for y, dsl_row in enumerate(dsl_lines):
            row = []
            dsl_cells = dsl_row.split("|")
            dsl_cells = [c for c in dsl_cells if c]
            for x, dsl_cell in enumerate(dsl_cells):
                tile_type = tile_type_dict[dsl_cell]
                row.append(tile_type(x, y, z) if tile_type else None)
            table.append(row)
        world_map.append(table)
