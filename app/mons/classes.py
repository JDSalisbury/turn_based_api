from faker import Faker
import random
from app.game_logic import Dice


class Move():

    def __init__(self, name, m_type, dmg, chance, d_type, cost, critical, description, stat_changes=[], effect_chance=0, effect=''):
        self.name = name
        self.m_type = m_type
        self.dmg = dmg
        self.chance = chance
        self.d_type = d_type
        self.critical = critical
        self.cost = cost
        self.description = description
        self.stat_changes = stat_changes
        self.effect = effect
        self.effect_chance = effect_chance


class MonManager(Dice):
    class Meta:
        abstract = True

    LOW_MOVE_LIST = [
        Move('Pound', 'Attack', 40, 100, 'physical', 4, 10, "Normal DMG Attack"),
        Move('Tackle', 'Attack', 30, 100, 'physical', 2, 0, "Normal DMG Attack"),
        Move('Slash', 'Attack', 30, 80, 'physical', 5, 50, "Normal DMG Attack"),
        Move('Bite', 'Attack', 50, 65, 'physical', 3, 0, "Normal DMG Attack"),
    ]

    MOVE_LIST = [
        Move('Trample', 'Attack', 45, 100,
             'physical', 6, 20, "Normal DMG Attack"),
        Move('DropKick', 'Attack', 60, 100,
             'physical', 10, 5, "Normal DMG Attack"),
        Move('Xslash', 'Attack', 30, 80, 'physical',
             10, 90, "Normal DMG Attack"),
        Move('Horn Attack', 'Attack', 50, 75,
             'physical', 5, 5, "Normal DMG Attack"),
        Move('Chomp', 'Attack', 100, 65, 'physical',
             12, 10, "Normal DMG Attack"),
    ]

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
    def random_moves(self, list, num=4):
        moves = []
        for _ in range(num):
            move = random.choice(list)
            if move not in moves:
                moves.append(move)
        return moves

    @classmethod
    def create_random_mon(self, start, stop, move_list):

        lvl = random.randrange(start, stop + 1)
        fake = Faker()
        mon = {}
        mon["name"] = fake.name()
        mon["lvl"] = lvl
        mon["hp"] = self.dice_roll(2, 6, lvl)
        mon["ATK"] = self.stats(lvl)
        mon["DEF"] = self.stats(lvl)
        mon["SPD"] = self.stats(lvl)
        mon["DEX"] = self.stats(lvl)
        mon["LUC"] = self.stats(lvl)

        mon['moves'] = move_list
        return mon


class LowLvlMon(MonManager):

    @classmethod
    def random_mon(self):
        return self.create_random_mon(1, 5, self.random_moves(self.MOVE_LIST, 3))


class MidLvlMon(MonManager):

    @classmethod
    def mid_lvl_moves(self):
        low_lvl = self.random_moves(self.LOW_MOVE_LIST, 1)
        mid_lvl = self.random_moves(self.MOVE_LIST, 3)
        return low_lvl + mid_lvl

    @classmethod
    def random_mon(self):
        return self.create_random_mon(5, 10, self.mid_lvl_moves())
