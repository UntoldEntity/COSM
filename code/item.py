# manage blocks
from enum import IntEnum

from sqlalchemy import true


class Item:
    def __init__(self, itemid, isDiamondFire):
        self.item = itemid
        self.diamondfire = isDiamondFire

class ValueType(IntEnum):
    TEXT = 0
    NUMBER = 1
    LOCATION = 2
    VECTOR = 3
    SOUND = 4
    PARTICLE = 5
    POTION_EFFECT = 6
    VARIABLE = 7
    GAME_VALUE = 8
    
    item = {
        0: "book",
        1: "slime_ball",
        2: "paper",
        3: "prismarine_shard",
        4: "nautilus_shell",
        5: "white_dye",
        6: "dragon_breath",
        7: "magma_cream",
        8: "name_tag",
    }
    
    @classmethod
    def valueTypeToItem():
        self.item[self.value]

class Value(Item):
    def __init__(self, ValueType): 
        self.diamondfire = true
        self.item = ValueType.valueTypeToItem()
        self.valueType = ValueType