from dataclasses import dataclass
from enum import Enum

"""Tokens

    This module defines the tokens used in the basic calculator.
    NUMBER: returns the number as a float.
"""

class TokenType(Enum):
    NUMBER = 0 
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    
@dataclass
class Token:
    type: TokenType
    value: any = None
    
    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value != None else "")
    