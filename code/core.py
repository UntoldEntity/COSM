from enum import IntEnum
from item import Item
class CodeBlockType(IntEnum):
    
    PLAYER_EVENT = 0
    ENTITY_EVENT = 1
    IF_PLAYER = 1000
    IF_ENTITY = 1001
    IF_VAR = 1002
    IF_GAME = 1003
    ELSE = 1004
    REPEAT = 1005
    PLAYER_ACTION = 2000
    ENTITY_ACTION = 2001
    GAME_ACTION = 2002
    DECLARE_FUNCTION = 3000
    DECLARE_PROCESS = 3001
    CALL_FUNCTION = 3100
    CALL_PROCESS = 3101
    SELECT_OBJECT = 4000
    CONTROL = 4001 
    SET_VARIABLE = 4002

class DiamondFireCodeBlock:
    def __init__(self, CodeBlockType, CodeAction):
        self.blocktype = CodeBlockType
        self.action = CodeAction
    chest = [Block(air)] * 27
    