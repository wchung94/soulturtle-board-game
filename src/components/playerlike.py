"""Shared type definitions for SoulTurtles components."""

from typing import Protocol


class PlayerLike(Protocol):
    """Protocol defining the interface for entities that cards can affect."""
    
    position: int
    soul_tokens: int
    name: str
    

    def move(self, steps: int, board_size: int) -> None:
        """Move the player forward."""
        ...
