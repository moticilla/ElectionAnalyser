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