from enum import IntEnum

class CodeBlockType(IntEnum):
    
    PLAYER_EVENT = 0
    ENTITY_EVENT = 1
    IF_PLAYER = 1000
    IF_ENTITY = 1001
    IF_VAR = 1002
    PLAYER_ACTION = 2000
    ENTITY_ACTION = 2001
    GAME_ACTION = 2002
    DECLARE_FUNCTION = 3000
    DECLARE_PROCESS = 3001
    CALL_FUNCTION = 3100
    CALL_PROCESS = 3101
    PLAYER_EVENT = 0
    PLAYER_EVENT = 0
    PLAYER_EVENT = 0

class DiamondFireCodeBlock:
    def __init__(self, CodeBlockType, CodeAction):
        self.blocktype = CodeBlockType
        self.action = CodeAction
    
    