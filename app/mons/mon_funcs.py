from faker import Faker
import random

def dice_roll(number_of_dice, dice_sides, mod):
    import random
    total = 0
    for i in range(1, number_of_dice + 1):
        total += random.randint(1, dice_sides)
    return total + mod


def stats(lvl):
    return dice_roll(lvl, 6, lvl)



def create_random_mon(start, stop, move_list):

    lvl = random.randrange(start, stop + 1) 
    fake = Faker()        
    mon = {}
    mon["name"] = fake.name()
    mon["lvl"] = lvl
    mon["hp"] = dice_roll(2, 6, lvl)
    mon['mana'] = dice_roll(3, 10, 10)
    mon["ATK"] = stats(lvl)
    mon["DEF"] = stats(lvl)
    mon["MAG"] = stats(lvl)
    mon["MDF"] = stats(lvl)
    mon["SPD"] = stats(lvl)
    moves = []
    for _ in range(4):
        move = random.choice(move_list)
        if move not in moves:
            moves.append(move)
    mon['moves'] = moves
    return mon