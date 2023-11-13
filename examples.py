from election import Election

election = Election([0, 1, 1, 0])
election.compute_and_print_payoffs()
print(election)

election = Election.create_from_string("0211110")
print(election)
election.compute_and_print_payoffs()

election = Election.create_from_count_and_positions(6, [1,2,4,5])
print(election)
election.compute_and_print_payoffs()

# Example usage:
num_players = 2
num_spaces = 10
equilibrium_exists, election = Election.find_equilibrium(num_players, num_spaces)

Election.print_equilibrium(*Election.find_equilibrium(2,4))

Election.print_equilibrium(*Election.find_equilibrium(3,9))

Election.create_from_string("0 1 1 0")