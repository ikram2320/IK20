from enum import Enum


class ItemType(Enum):
    healing_potion = 0
    attack_boost = 1
    defense_boost = 2


class Item(object):
    def __init__(self, name, Type: ItemType, boost_points: int, description):
        self.name = name
        self.Type = Type
        self.boost_points = boost_points
        self.description = description
