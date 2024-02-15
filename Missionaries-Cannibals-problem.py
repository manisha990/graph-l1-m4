#************** Correct one *************************

# initial configuration (3 missionaries and cannibals on bank 1)
bank1 = {'c': 3, 'm': 3}
bank2 = {'c': 0, 'm': 0}
boat = {'c': 0, 'm': 0}

# Function to print the state of each configuration
def print_state(dct1, dct2, dct3):
    """
        Prints each configuration in easily readable form
    """

    print(f"Bank 1: {bank1['c']} cannibal(s), {bank1['m']} missionary/ies")
    print(f"Bank 2: {bank2['c']} cannibal(s), {bank2['m']} missionary/ies")
    print(f"Boat: {boat['c']} cannibal(s), {boat['m']} missionary/ies")
    print()


def cann_miss(b1=bank1, b2=bank2, bo=boat):
    # crossing logic
    if all(x == 0 for x in b2.values()):  # bank2 is empty
        print_state(b1, b2, bo)
        b1['c'] -= 1  # 1 cannibal leaves bank1 and ...
        bo['c'] += 1  # ... goes on board

    b1['m'] -= 1  # 1 missionary leaves bank1 and ...
    bo['m'] += 1  # ... goes on board
    print_state(b1, b2, bo)

    if all(x == 0 for x in b1.values()):  # bank1 is empty
        bo['c'], bo['m'] = 0, 0  # 1 cannibal and 1 missionary go out of boat
        b2['c'] += 1  # 1 cannibal steps out on bank2
        b2['m'] += 1  # 1 missionary steps out on bank2
        print_state(b1, b2, bo)
        return  # final condition is met

    bo['m'] -= 1  # 1 missionary goes out of boat and ...
    b2['m'] += 1  # ... steps out on bank2
    print_state(b1, b2, bo)

    b1['c'] -= 1  # 1 cannibal leaves bank1 and ...
    bo['c'] += 1  # ... goes on board
    print_state(b1, b2, bo)

    bo['c'] -= 1  # 1 cannibal goes out of boat and ...
    b2['c'] += 1  # ... steps out on bank2
    print_state(b1, b2, bo)

    # Recur for another series of crossings
    cann_miss(b1, b2, bo)  # another series of crossings

# Main function
def main():
    cann_miss()

# Enter point
if __name__ == '__main__':
    main()