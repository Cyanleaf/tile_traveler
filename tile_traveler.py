"""
https://github.com/Kristjan-O-Ragnarsson/tile_traveler
tile taveler a til movement program move betvine tiles in a 3x3 env
"""

def valid_directions(x, y):
    """
    returns valid directions for player in string format
    """
    print(x == 1, y)
    valid = "nesw"
    if x == 1:
        valid = valid.replace("w", "")
    if y == 1:
        valid = valid.replace("s", "")
    if x == 3:
        valid = valid.replace("e", "")
    if y == 3:
        valid = valid.replace("n", "")
    print(valid)
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
    valid = valid_directions(x, y)
    print(valid)
    print("You can travel: ", end="")
    to_print = ""
    for i in valid:
        if i == valid[-1] and i != valid[0]:
            to_print += " or"
        if i == "n":
            to_print += " (N)orth "
        elif i == "e":
            to_print += " (E)ast "
        elif i == "s":
            to_print += " (S)outh "
        elif i == "w":
            to_print += " (W)est "
        
    print(to_print + ".")


def move_player(user_input, x, y):
    valid = valid_directions()
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
        
            


x = 1
y = 1

kill = False

while not kill:
    valid_travel_print(x, y)
    user_input = input("Direction: ")
    
    if x == 3 and y == 1:
        print("Victory!")
        kill = True