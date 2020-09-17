"""
https://github.com/Kristjan-O-Ragnarsson/tile_traveler
tile taveler a til movement program move betvine tiles in a 3x3 env
"""

def valid_directions():
    """
    returns valid directions for player in string format
    """
    valid = "nesw"
    if x == 1:
        valid.replace("w", "")
    if y == 1:
        valid.replace("s", "")
    if x == 3:
        valid.replace("e", "")
    if y == 3:
        valid.replace("n", "")
    
    if x == 1 and y == 1:
        valid.replace("e", "")
    elif x == 2 and y == 1:
        valid.replace("e", "")
        valid.replace("w", "")
    elif x == 2 and y == 2:
        valid.replace("n", "")
        valid.replace("e", "")
    elif x == 2 and y == 3:
        valid.replace("s", "")
    elif x == 3 and y == 2:
        valid.replace("w", "")

    return valid

def move_player(user_input):
    pass

x = 1
y = 1

kill = False

while not kill:
    user_input = input("Direction: ")
    
    if posision_3_1:
        print("Victory!")
        kill = True