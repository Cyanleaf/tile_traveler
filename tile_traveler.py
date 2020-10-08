"""
https://github.com/Cyanleaf/tile_traveler
tile taveler a til movement program move betvine tiles in a 3x3 env
"""

import random

def valid_directions(x, y):
    """
    returns valid directions for player in string format
    """
    #print(x == 1, y)
    valid = "nesw"
    if x == 1:
        valid = valid.replace("w", "")
    if y == 1:
        valid = valid.replace("s", "")
    if x == 3:
        valid = valid.replace("e", "")
    if y == 3:
        valid = valid.replace("n", "")
    #print(valid)
    if x == 1 and y == 1:
        valid = valid.replace("e", "")
    elif x == 2 and y == 1:
        valid = valid.replace("e", "")
        valid = valid.replace("w", "")
    elif x == 2 and y == 2:
        valid = valid.replace("n", "")
        valid = valid.replace("e", "")
    elif x == 2 and y == 3:
        valid = valid.replace("s", "")
    elif x == 3 and y == 2:
        valid = valid.replace("w", "")

    return valid

def valid_travel_print(x, y):
    """
    prints the valid directgion for the player
    t.d. You can travel: (N)orth.
         You can travel: (N)orth or (S)outh.
    """
    valid = valid_directions(x, y)
    #print(valid)
    print("You can travel:", end="")
    to_print = ""
    for i in valid:
        if i != valid[0]:
            to_print += " or"
        if i == "n":
            to_print += " (N)orth"
        elif i == "e":
            to_print += " (E)ast"
        elif i == "s":
            to_print += " (S)outh"
        elif i == "w":
            to_print += " (W)est"
        
    print(to_print + ".")


def move_player(user_input, x, y):
    """
    changes the player coordinets according to user input
    returns new x and y coordinets
    """
    valid = valid_directions(x, y)
    user_input_clean = user_input.strip().lower()
    if user_input_clean in valid:
        if user_input_clean == "s":
            y -= 1
        elif user_input_clean == "w":
            x -= 1
        elif user_input_clean == "n":
            y += 1
        elif user_input_clean == "e":
            x += 1
        prev_pos[0] = False
    else:
        prev_pos[0] = True
        print("Not a valid direction!")
    
    return (x, y)

def lever_logic(coins, coin_pos):
    pull_lever = random.choice(["YES", "NO"])
    print('Pull a lever (y/n): {}'.format(pull_lever[0].lower()))
    if pull_lever == 'YES':
        coins += 1
        print('You received 1 coin, your total is now {}.'.format(coins))
    return coins

def lever_positions(x, y, coins):
    if x == 1 and y == 2:
        coins = lever_logic(coins, 0)
    elif x == 2 and y == 2:
        coins = lever_logic(coins, 1)
    elif x == 2 and y == 3:
        coins = lever_logic(coins, 2)
    elif x == 3 and y == 2:
        coins = lever_logic(coins, 3)
    return coins


prev_pos = [False]

def game_logic():
    random_seed = int(input("Input seed: "))
    random.seed(random_seed)
    x = 1
    y = 1
    coins = 0
    kill = False
    moves = 0
    while not kill:
        valid_travel_print(x, y)
        direction = random.choice(["NORTH", "EAST", "SOUTH", "WEST"])
        user_input = direction[0].lower()
        print('Direction: {}'.format(user_input))
        moves += 1

        x, y = move_player(user_input, x, y)
        if not prev_pos[0]:
            coins = lever_positions(x, y, coins)

        # Victory condition
        if x == 3 and y == 1:
            print("Victory! Total coins {}. Moves {}.".format(coins, moves))
            kill = True

def main():
    while True:
        game_logic()
        cmd = input('Play again (y/n): ').strip()
        if cmd.lower() != 'y':
            break
        else:
            prev_pos[0] = False

main()