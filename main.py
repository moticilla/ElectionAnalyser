from election import Election
        



election = Election.create_from_string("1231")
print(election.check_equilibrium())


s = 1
while True:
    Election.print_all_equilibria(12,s)
    s += 1

#print_all_equilibria(3,4)

#print_all_equilibria(3,4)

