import random
from faker import Faker
from .mon_funcs import *


class MonManager:
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

class LowLvlMons(MonManager):

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
        return create_random_mon(1, 5, self.MOVE_LIST)

class MidLvlMons(MonManager):

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
        return create_random_mon(5, 10, self.MOVE_LIST)