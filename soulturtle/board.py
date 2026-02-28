"""Board and Space definitions for SoulTurtles."""

from dataclasses import dataclass, field
from enum import Enum, auto


class SpaceType(Enum):
    NORMAL = auto()
    BOOST = auto()
    PENALTY = auto()
    WARP = auto()
    START = auto()
    FINISH = auto()


@dataclass
class Space:
    """A single space on the board."""

    index: int
    space_type: SpaceType = SpaceType.NORMAL
    effect: int = 0
    warp_target: int | None = None

    def apply(self, position: int) -> tuple[int, int]:
        """Apply the space effect and return (new_position, soul_delta)."""
        if self.space_type == SpaceType.BOOST:
            return position + self.effect, 0
        if self.space_type == SpaceType.PENALTY:
            return max(0, position - self.effect), 0
        if self.space_type == SpaceType.WARP and self.warp_target is not None:
            return self.warp_target, 0
        return position, self.effect


class Board:
    """Represents the SoulTurtles game board."""

    def __init__(self, spaces: list[Space] | None = None) -> None:
        if spaces is not None:
            self._spaces = spaces
        else:
            self._spaces = self._default_board()

    def _default_board(self) -> list[Space]:
        """Build the default 30-space board."""
        spaces = [Space(i) for i in range(31)]
        spaces[0].space_type = SpaceType.START
        spaces[30].space_type = SpaceType.FINISH

        # A few boost and penalty spaces
        for idx in (5, 15, 25):
            spaces[idx].space_type = SpaceType.BOOST
            spaces[idx].effect = 3

        for idx in (10, 20):
            spaces[idx].space_type = SpaceType.PENALTY
            spaces[idx].effect = 2

        # A warp space
        spaces[8].space_type = SpaceType.WARP
        spaces[8].warp_target = 18

        return spaces

    @property
    def size(self) -> int:
        """Number of spaces on the board (excluding the finish space)."""
        return len(self._spaces) - 1

    def get_space(self, index: int) -> Space:
        """Return the Space at *index*, clamping to the finish space."""
        index = min(index, self.size)
        return self._spaces[index]
