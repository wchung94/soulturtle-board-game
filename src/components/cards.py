from dataclasses import dataclass
from enum import Enum, auto
from typing import NamedTuple

@dataclass
class Card():
    def __init__(self, name: str, description: str, effect_id: int):
        self.name = name
        self.description = description
        self.effect_id = effect_id  # Identifier for the card's effect

    def __repr__(self):
        return f"Card(name='{self.name}', description='{self.description}', effect_id={self.effect_id})"
    

@dataclass
class EventCard(Card):
    pass  # Additional attributes or methods specific to Event cards can be added here

@dataclass
class LocationCard(Card):
    pass  # Additional attributes or methods specific to Location cards can be added here

@dataclass
class EntityCard(Card):
    pass  # Additional attributes or methods specific to Entity cards can be added here 