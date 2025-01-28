# Import the necessary libraries
from enum import IntEnum, auto

# Create a new class called Layer that inherits from IntEnum.
class Layer(IntEnum):
    "'Enum for the layers in the game'"
    BACKGROUND = auto()
    OBSTACLE = auto()
    FLOOR = auto()
    PLAYER = auto()
    UI = auto()
