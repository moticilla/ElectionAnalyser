
import numpy as np


class Election:

    def __init__(self, layout: list[int]):
        self.layout = np.array(layout)
        self.players_at_space = {}
        self.space_of_player = {}
        # Assign players numbers
        player = 0
        for space in range(len(layout)):
            players_at_space = layout[space]
            if players_at_space != 0:
                for _ in range(players_at_space):
                    self.space_of_player[player] = space
                    player += 1
                self.players_at_space[space] = players_at_space
        self.no_players = len(self.players_at_space.keys())

    @classmethod
    def create_from_string(self, str_layout: str):
        layout = []
        for char in str_layout:
            layout.append(int(char))
        return Election(layout)
    
    @classmethod
    def create_from_count_and_positions(self, count, positions):
        # positions should be 0 indexed
        from collections import Counter
        layout = []
        pos_dict = Counter(positions)
        for space in range(count):
            if space in pos_dict:
                layout.append(int(pos_dict[space]))
            else:
                layout.append(0)
        return Election(layout)
    
    def get_space_payoffs(self):
        s = len(self.layout)
        space_payoffs = {}
        current_value = 0
        init_value = 0
        cur_player_bundle = None

        for space in range(s):
            if self.layout[space] != 0:
                # old bundle
                if cur_player_bundle is None:
                    init_value = current_value
                else:
                    space_payoffs[cur_player_bundle] += current_value/2
                    init_value = current_value/2
                # new bundle
                cur_player_bundle = space
                space_payoffs[cur_player_bundle] = init_value + 1
                init_value = 0
                current_value = 0
            else:
                current_value += 1

        space_payoffs[cur_player_bundle] += current_value
        return space_payoffs
    
    def get_player_payoffs(self):
        space_payoffs = self.get_space_payoffs()
        player_payoffs = {}
        for player, space in self.space_of_player.items():
            player_payoffs[player] = (space_payoffs[space] /
                                      self.players_at_space[space])
        return player_payoffs
    
    def compute_and_print_payoffs(self):
        # We shouldn't compute each time, but alas
        player_payoffs = self.get_player_payoffs()
        self.print_payoffs(player_payoffs)

    def print_payoffs(self, player_payoffs):
        for player, payoff in player_payoffs.items():
            print(player, "@", self.space_of_player[player], ": ", payoff)

    def __str__(self):
        str_layout = ""
        for num in self.layout:
            str_layout += str(num) + " "
        return str_layout


