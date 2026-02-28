"""Player model for SoulTurtles."""

from dataclasses import dataclass, field


@dataclass
class Player:
    """Represents a player in the SoulTurtles game."""

    name: str
    position: int = 0
    soul_tokens: int = 0
    is_finished: bool = False

    def move(self, steps: int, board_size: int) -> None:
        """Advance the player by *steps*, capping at board_size."""
        self.position = min(self.position + steps, board_size)
        if self.position >= board_size:
            self.is_finished = True

    def apply_soul_delta(self, delta: int) -> None:
        """Adjust soul token count, flooring at zero."""
        self.soul_tokens = max(0, self.soul_tokens + delta)

    def reset(self) -> None:
        """Reset the player to starting state."""
        self.position = 0
        self.soul_tokens = 0
        self.is_finished = False
