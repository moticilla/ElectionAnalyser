import numpy as np
from copy import deepcopy
#Number of players
n = 3
#Number of spaces
s = 4
myList = np.array([0,2,1,1,1,1,1,0])
s = len(myList)
space_payoffs = {}

current_value = 0
init_value = 0
cur_player_bundle = None

for space in range(s):
    if myList[space] != 0:
        # old bundle
        if cur_player_bundle is None:
            init_value = current_value
        else:
            space_payoffs[cur_player_bundle] += current_value/2
            init_value = current_value/2
        # new bundle
        cur_player_bundle = space
        space_payoffs[cur_player_bundle] = deepcopy(init_value + 1)
        init_value = 0
        current_value = 0
    else:
        current_value += 1

space_payoffs[cur_player_bundle] += current_value

for position, value in space_payoffs.items():
    print(position, ": ", value)

