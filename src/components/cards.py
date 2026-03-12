from dataclasses import dataclass
from enum import Enum, auto
from .playerlike import PlayerLike

class card_type(Enum):
    """Enumeration for card types."""
    ENTITY = auto()
    LOCATION = auto()
    EVENT = auto()

class Card():
    def __init__(self, name: str, tag: str, description: str, effect_id: int, card_type: card_type):
        self.name = name
        self.tag = tag
        self.description = description
        self.type = card_type
        self.effect_id = effect_id  # Identifier for the card's effect

    def __repr__(self):
        return f"Card(name='{self.name}', description='{self.description}', effect_id={self.effect_id}, type={self.type.name})"

    def apply_effect(self, player: PlayerLike):
        """Apply the card's effect to the given player."""
        # Placeholder for effect application logic based on effect_id
        pass

