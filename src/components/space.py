from dataclasses import dataclass
from enum import Enum, auto
from typing import NamedTuple

class SpaceType(Enum):
    """"Type of space on the board, affecting player movement and soul tokens.
    auto() is used to automatically assign unique values to each enum member."""
    NORMAL = auto()
    # EVENT = auto()
    # LOCATION = auto()
    # ENTITY = auto()
    ACTION = auto()
    START = auto()
    FINISH = auto()


class HexCoord(NamedTuple):
    """Axial coordinate for a hexagonal grid."""
    q: int
    r: int


@dataclass
class Space:
    """A single space on the board."""

    index: int
    space_type: SpaceType = SpaceType.NORMAL
    effect: int = 0 # define which Event/Location/Entity card to draw when space type is ACTION
    hex_coord: HexCoord | None = None
