"""Board and Space definitions for SoulTurtles."""

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


class Board:
    """Represents the SoulTurtles hexagonal game board with n/sides = x spaces and cubic coordinates
    3n(n−1)+1 spaces in total, where n is the number of hexagons per side. For n=6, there are 91 spaces.
    """

    def __init__(self, sides: int = 6) -> None:
        self.sides = sides
        self._spaces = self._default_board(self.sides)

    @staticmethod
    def _generate_hex_board(n: int) -> list[HexCoord]:
        """Generate 3n(n−1)+1 hexagonal coordinates in a hexagon shape with n hexagons per side.
        
        Uses axial coordinates where valid points satisfy max(|q|, |r|, |q+r|) <= n-1.
        This creates a hexagon with radius n-1 (side length n) for 3*n² - 3*n + 1 spaces.
        """
        coords = []
        
        # Generate all hexagons where max(|q|, |r|, |q+r|) <= n-1
        for q in range(-n + 1, n):
            for r in range(-n + 1, n):
                if max(abs(q), abs(r), abs(q + r)) <= n - 1:
                    coords.append(HexCoord(q, r))
        return coords

    def _default_board(self, sides: int) -> list[Space]:
        """Build the default hexagonal board with 3n(n−1)+1 spaces (n hexagons per side)."""
        hex_coords = self._generate_hex_board(sides)
        spaces = [Space(i, hex_coord=coord) for i, coord in enumerate(hex_coords)]

        num_spaces = len(spaces)
        radius = sides - 1
        
        # Set the 6 corner hexagons as START spaces
        corner_coords = [
            HexCoord(radius, -radius),   # top right
            HexCoord(radius, 0),          # right
            HexCoord(0, radius),          # bottom right
            HexCoord(-radius, radius),   # bottom left
            HexCoord(-radius, 0),         # left
            HexCoord(0, -radius),         # top left
        ]
        
        # Set the center hexagon as the FINISH space
        center_coord = HexCoord(0, 0)
        
        # Set space types based on coordinates
        for space in spaces:
            if space.hex_coord in corner_coords:
                space.space_type = SpaceType.START
            elif space.hex_coord == center_coord:
                space.space_type = SpaceType.FINISH
            # Add ACTION spaces distributed throughout the board
            # Place 50/50 ACTION / NORMAL  spaces at regular intervals
            else:
                random_value = (space.index * 7) % 100  # Deterministic pseudo-random value based on index
                if random_value < 50:  # 50% chance to become an ACTION space
                    space.space_type = SpaceType.ACTION
                    space.effect = random_value % 3 + 1  # Placeholder effect ID (1,2,3) for ACTION spaces
                else:
                    space.space_type = SpaceType.NORMAL

        return spaces

    @property
    def size(self) -> int:
        """Number of spaces on the board (excluding the finish space)."""
        return len(self._spaces) - 1

    def get_space(self, index: int) -> Space:
        """Return the Space at *index*, clamping to the finish space."""
        index = min(index, self.size)
        return self._spaces[index]

    def get_neighbors(self, index: int) -> list[int]:
        """Return indices of neighboring hexagonal spaces."""
        if index < 0 or index >= len(self._spaces):
            return []

        space = self._spaces[index]
        if space.hex_coord is None:
            return []

        q, r = space.hex_coord
        # Hexagonal neighbors in axial coordinates
        neighbor_coords = [
            HexCoord(q + 1, r),
            HexCoord(q - 1, r),
            HexCoord(q, r + 1),
            HexCoord(q, r - 1),
            HexCoord(q + 1, r - 1),
            HexCoord(q - 1, r + 1),
        ]

        neighbors = []
        for coord in neighbor_coords:
            for i, space_item in enumerate(self._spaces):
                if space_item.hex_coord == coord:
                    neighbors.append(i)
                    break
        return neighbors

    def _to_pretty_string(self) -> str:
        """Return a printable text representation of the hexagonal board."""
        radius = self.sides - 1
        coord_to_space = {space.hex_coord: space for space in self._spaces if space.hex_coord is not None}

        symbols = {
            SpaceType.NORMAL: ".",
            SpaceType.ACTION: "A",
            SpaceType.START: "S",
            SpaceType.FINISH: "F",
        }

        lines: list[str] = []
        for r in range(-radius, radius + 1):
            row_cells: list[str] = []
            for q in range(-radius, radius + 1):
                if max(abs(q), abs(r), abs(q + r)) > radius:
                    continue

                space = coord_to_space.get(HexCoord(q, r))
                if space is None:
                    continue

                row_cells.append(f"{space.index:02}{symbols[space.space_type]}")

            indent = "   " * abs(r)
            lines.append(f"{indent}{' '.join(row_cells)}")

        return "\n".join(lines)

    def print_board(self) -> None:
        """Print the board in a human-readable hexagonal layout."""
        print(self._to_pretty_string())


if __name__ == "__main__":
    board = Board(sides=5)
    board.print_board()