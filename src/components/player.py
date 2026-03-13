"""Player model for SoulTurtles."""

from dataclasses import dataclass, field
from .space import SpaceType, HexCoord, Space    



@dataclass
class PlayerStats:
    """Represents the statistics of a player."""
    strength: int = 0
    agility: int = 0
    charisma: int = 0
    position: HexCoord = HexCoord(0, 0)
    coins : int = 0
    penalty : list[str] = field(default_factory=list)

class Player:
    """Represents a player in the SoulTurtles game."""
    def __init__(self, name: str, stats: PlayerStats | None = None):
        self.name: str = name
        self.turns_taken: int = 0
        self.is_finished: bool = False
        self.stats: PlayerStats = stats if stats is not None else PlayerStats()  # For tracking additional stats if needed

    def move(self, steps: int, board_size: int) -> None:
        """Advance the player by *steps*, capping at board_size."""
        # Convert HexCoord to a linear index for movement
        current_index = self.stats.position.q + self.stats.position.r  # Simplified linear index
        new_index = min(current_index + steps, board_size)
        self.stats.position = HexCoord(new_index, new_index)  # Update position with new HexCoord
        if new_index >= board_size:
            self.is_finished = True

    def apply_coin_delta(self, delta: int) -> None:
        """Adjust coin count, flooring at zero."""
        self.stats.coins = max(0, self.stats.coins + delta)

    def reset(self) -> None:
        """Reset the player to starting state."""
        self.stats.position = HexCoord(0, 0)
        self.stats.coins = 0
        self.is_finished = False

    def __repr__(self, *args, **kwds):
        return f"Player(name={self.name}, stats={self.stats})"

class Milan(Player):
    """Represents the special player Milan with unique abilities."""
    # Placeholder for Milan-specific attributes and methods
    pass

class Rody(Player):
    """Represents the special player Rody with unique abilities."""
    # Placeholder for Rody-specific attributes and methods
    pass

class Charlie(Player):
    """Represents the special player Charlie with unique abilities."""
    # Placeholder for Charlie-specific attributes and methods
    pass


if __name__ == "__main__":
    milan_stats = PlayerStats(strength=3, agility=2, charisma=4, position=HexCoord(1, 1), coins=5)
    milan = Player("Milan", stats=milan_stats)
    print(milan)
