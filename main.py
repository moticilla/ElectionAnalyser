from election import Election

def print_all_equilibria(players, spaces):
    found_any, equilibria = Election.thorough_find_all_equilibria(players,spaces)

    if found_any:
        print(f"Equilibria for {players} players and {spaces} spaces:")
        for equi in equilibria:
            print(equi)
    else:
        print(f"There are no equilibria for {players} players and {spaces} spaces.")
        



# election = Election.create_from_string("00110100110")
# print(election.check_equilibrium())
s = 1
while True:
    print_all_equilibria(5,s)
    s += 1