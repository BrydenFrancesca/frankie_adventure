import random
import enemies
import items
import npc
import tile_descriptions as td
import basement_tiles as tb

###Abbreviated map
world_basement = """
|DT|  |DT|DT|
|DT|DT|DT|DT|
|DT|DT|DT|DT|
|  |DT|DT|WT|

"""

world_first_floor = """
|UT|  |ET|KT|
|OT|ST|OT|ET|
|ET|ET|KT|ET|
|  |KT|OT|TT|

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
                   "DT": tb.BasementTile,
                   "  ": None}

##Layout the grid of the map
world_map = []

#Define automated map function
def parse_world_dsl():
    z = -1
    for ta in [world_basement, world_first_floor]:
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
