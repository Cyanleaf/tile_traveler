"""
https://github.com/Kristjan-O-Ragnarsson/tile_traveler
tile taveler a til movement program move betvine tiles in a 3x3 env
"""



posision_1_1 = True
posision_1_2 = False
posision_1_3 = False
posision_2_1 = False
posision_2_2 = False
posision_2_3 = False
posision_3_1 = False
posision_3_2 = False
posision_3_3 = False

kill = False

while not kill:
    user_input = input("Direction: ")
    
    if posision_3_1:
        print("Victory!")
        kill = True