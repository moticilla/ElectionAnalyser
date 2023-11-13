
import numpy as np
import random
from itertools import combinations_with_replacement


class Election:

    def __init__(self, layout):
        self.layout = np.array(layout)
        self.space_of_player = {}
        # Assign players numbers
        player = 0
        for space in range(len(layout)):
            players_at_space = layout[space]
            if players_at_space != 0:
                for _ in range(players_at_space):
                    self.space_of_player[player] = space
                    player += 1
        self.no_players = player + 1

    @classmethod
    def create_from_string(self, str_layout: str):
        layout = []
        str_layout = str_layout.replace(" ", "")
        for char in str_layout:
            layout.append(int(char))
        return Election(layout)
    
    @classmethod
    def combine_elections(self, *elections):
        elecstr = ""
        for x in elections:
            elecstr += (str(x))
        return Election.create_from_string(elecstr)

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
    
    def move_player(self, player, new_space):
        old_space = self.space_of_player[player]
        self.layout[old_space] -= 1
        self.layout[new_space] += 1
        self.space_of_player[player] = new_space
    
    def get_player_payoffs(self):
        space_payoffs = self.get_space_payoffs()
        player_payoffs = {}
        for player, space in self.space_of_player.items():
            player_payoffs[player] = (space_payoffs[space] /
                                      self.layout[space])
        return player_payoffs
    
    def check_equilibrium(self):
        equilibrium = True

        for player in self.space_of_player.keys():
            current_position = self.space_of_player[player]
            current_payoff = self.get_player_payoffs()[player]

            for space in range(len(self.layout)):
                # Create a new Election object for each iteration (do we strictly need to create a new one, or could we just store the original and restore when needed?)
                new_election = Election(self.layout.copy())
                new_election.space_of_player = self.space_of_player.copy()

                # Move the player to the new space
                new_election.move_player(player, space)

                new_payoff = new_election.get_player_payoffs()[player]

                if new_payoff > current_payoff:
                    equilibrium = False
                    break  # No need to continue checking other spaces

        return equilibrium

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
    
    @classmethod
    def random_find_equilibrium(self, num_players, num_spaces, max_attempts=1000):
        """
        Attempt to find an equilibirum through random placement. Fails after a specified number of maximum attempts.
        """
        for _ in range(max_attempts):
            # Place players randomly in the initial layout (so this random placement could have duplicates?)
            players_positions = random.sample(range(num_spaces), num_players)

            # Create an Election object with the initial layout
            election = Election.create_from_count_and_positions(num_spaces, players_positions)

            # Check for equilibrium
            is_equilibrium = election.check_equilibrium()

            if is_equilibrium:
                return is_equilibrium, election

        # If no equilibrium is found after max_attempts, return False, and a None Election
        return False, None
    
    @classmethod
    def thorough_find_equilibrium(self, num_players, num_spaces):
        """
        Find an equilibrium in the specified setting.
        """
        for players_positions in combinations_with_replacement(range(num_spaces), num_players):
            election = Election.create_from_count_and_positions(num_spaces, players_positions)

            # Check for equilibrium
            is_equilibrium = election.check_equilibrium()

            if is_equilibrium:
                return is_equilibrium, election

        # If no equilibrium is found after max_attempts, return False, and a None Election
        return False, None
    
    @classmethod
    def thorough_find_all_equilibria(self, num_players, num_spaces):
        """
        Find all equilibria in the specified setting.
        """
        equilibria = []
        for players_positions in combinations_with_replacement(range(num_spaces), num_players):
            election = Election.create_from_count_and_positions(num_spaces, players_positions)

            # Check for equilibrium
            is_equilibrium = election.check_equilibrium()

            if is_equilibrium:
                equilibria.append(election)

        # If no equilibrium is found after max_attempts, return False, and a None Election
        if equilibria:
            return True, equilibria
        else:
            return False, None
    
    @classmethod
    def print_equilibrium(self, equilibrium_exists, election):
        if equilibrium_exists:
            print("Is Equilibrium:", equilibrium_exists)
            print("Final Layout:", election)
            print("Player Payoffs:", election.get_player_payoffs())
        else:
            print("No equilibrium found after max attempts.")
            
            
    @classmethod
    def print_all_equilibria(self, players, spaces):
        found_any, equilibria = Election.thorough_find_all_equilibria(players,spaces)

        if found_any:
            print(f"Equilibria for {players} players and {spaces} spaces:")
            for equi in equilibria:
                print(equi)
        else:
            print(f"There are no equilibria for {players} players and {spaces} spaces.")