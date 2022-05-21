# manage blocks
from enum import IntEnum

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
    NONE = 9
    
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
        9: None
    }
    
    @classmethod
    def valueTypeToItem():
        self.item[self.value]

class VariableType(IntEnum):
    TEXT = 0
    NUMBER = 1
    LOCATION = 2
    VECTOR = 3
    SOUND = 4
    PARTICLE = 5
    POTION_EFFECT = 6
    VARIABLE = 7
    GAME_VALUE = 8
    LIST = 9
    NONE = 10
    

class Value(Item):
    def __init__(self, ValueType): 
        self.diamondfire = True
        self.item = ValueType.valueTypeToItem()
        self.valueType = ValueType

class Variable(Value):
    def __init__(self, VariableType):
        self.diamondfire = True
        self.item = "magma_cream"
        self.valueType = ValueType.VARIABLE
        self.variable.type = VariableType
        self.variable.value = None
        if VariableType == 9:
            self.variable.list = [None]