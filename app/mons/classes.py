from faker import Faker
import random
from app.game_logic import Dice

class MonManager(Dice):
    class Meta:
        abstract = True

    @classmethod
    def random_mon(self):
        return {
            "name": "Randal",
            "hp": 10,
            "mana": 100,
            "moves": [
                "Tackle",
                "Punch",
                "Kick",
                "Magic Missle"
            ]
        }



    @classmethod
    def stats(self, lvl):
        return self.dice_roll(lvl, 6, lvl)


    @classmethod
    def create_random_mon(self, start, stop, move_list):

        lvl = random.randrange(start, stop + 1) 
        fake = Faker()        
        mon = {}
        mon["name"] = fake.name()
        mon["lvl"] = lvl
        mon["hp"] = self.dice_roll(2, 6, lvl)
        mon['mana'] = self.dice_roll(3, 10, 10)
        mon["ATK"] = self.stats(lvl)
        mon["DEF"] = self.stats(lvl)
        mon["MAG"] = self.stats(lvl)
        mon["MDF"] = self.stats(lvl)
        mon["SPD"] = self.stats(lvl)
        moves = []
        for _ in range(4):
            move = random.choice(move_list)
            if move not in moves:
                moves.append(move)
        mon['moves'] = moves
        return mon


class Move():

    def __init__(self, lvl):
        self.name =''
        self.dmg = ''
        self.chance = ''
        self.d_type = ''
        self.cost = ''




class LowLvlMon(MonManager):

    MOVE_LIST = [
        {
            "name": "Takle",
            "type": "A",
            "dmg": "30",
            'chance': "90%"
        },
        {
            "name": "Tail whip",
            "type": "M",
            "dmg": "40",
            'chance': "65%"
        },
        {
            "name": "Slash",
            "type": "A",
            "dmg": "20",
            'chance': "100%"
        },
        {
            "name": "Stomp",
            "type": "M",
            "dmg": "50",
            'chance': "55%"
        },
        {
            "name": "Bite",
            "type": "A",
            "dmg": "15",
            'chance': "100%"
        }
    ]


    @classmethod
    def random_mon(self):
        return self.create_random_mon(1, 5, self.MOVE_LIST)

class MidLvlMon(MonManager):

    MOVE_LIST = [
        {
            "name": "Trample",
            "type": "A",
            "dmg": "45",
            'chance': "90%"
        },
        {
            "name": "DropKick",
            "type": "M",
            "dmg": "60",
            'chance': "65%"
        },
        {
            "name": "Xslash",
            "type": "A",
            "dmg": "35",
            'chance': "100%"
        },
        {
            "name": "Horn Attack",
            "type": "M",
            "dmg": "100",
            'chance': "55%"
        },
        {
            "name": "Chomp",
            "type": "A",
            "dmg": "30",
            'chance': "100%"
        }
    ]

    @classmethod
    def random_mon(self):
        return self.create_random_mon(5, 10, self.MOVE_LIST)