from election import Election

election = Election.create_from_string("1231")
print(election.check_equilibrium())


def print_all_equilibria_for_any_spaces(n):
    s = 1
    while True:
        Election.print_all_equilibria(n, s)
        s += 1


def print_all_equilibria_for_any_players(s):
    n = 1
    while True:
        Election.print_all_equilibria(n, s)
        n += 1


# print_all_equilibria(3,4)

# print_all_equilibria(3,4)


def split_layout(layout: str):
    new_layout = ""
    for char in layout:
        if char != "0":
            char = "9"
        new_layout += char

    middle_start = new_layout.find("9")
    middle_end = new_layout.rfind("9")

    if middle_start == -1 or middle_end == -1:
        print("Format incorrect")
        return None

    start = layout[0:middle_start]
    middle = layout[middle_start : middle_end + 1]
    end = layout[middle_end + 1 :]
    return start, middle, end


def add_player_between_every_internal_pair(e: Election):
    layout = str(e)
    start, middle, end = split_layout(layout)
    middle_modified = add_player_between_every_pair_in_layout(middle)
    layout_modified = start + middle_modified + end
    return Election.create_from_string(layout_modified)


def add_player_between_every_pair_in_layout(layout: str):
    return layout.replace(" ", "").replace("00", "010")


def check_add_player_equi(layout: str):
    election = Election.create_from_string(layout)
    new_election = add_player_between_every_internal_pair(election)
    print(new_election)
    return new_election.check_equilibrium()


# start, middle, end = split_layout("0010010")
# print(start, "|", middle, "|", end)
def check_layouts_addition_conjecture():
    layouts = [
        "01100110",
        "0 2 0 0 1 0 0 2 0",
        "0 0 0 2 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0 0",
        "0 1 1 0 0 1 0 0 2 0 0",
    ]

    for layout in layouts:
        if Election.create_from_string(layout).check_equilibrium():
            print(check_add_player_equi(layout))
        else:
            print("Layout ", layout, " is not an equilibrium.")


e = Election.create_from_string
A = "0110"
B = "001100"
print(Election.combine_elections(e(B), e(B), e(B), e(B)).check_equilibrium())

print_all_equilibria_for_any_players(10)
