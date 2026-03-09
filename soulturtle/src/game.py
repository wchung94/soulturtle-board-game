"""Game engine for SoulTurtles."""

import random
from dataclasses import dataclass, field

from .components.board import Board, SpaceType
from .components.player import Player


@dataclass
class GameResult:
    """Outcome of a completed game."""

    winner: str
    turn_count: int
    final_positions: dict[str, int] = field(default_factory=dict)
    final_soul_tokens: dict[str, int] = field(default_factory=dict)


class Game:
    """Manages a single play-through of SoulTurtles."""

    def __init__(
        self,
        players: list[Player],
        board: Board | None = None,
        dice_sides: int = 6,
        rng: random.Random | None = None,
    ) -> None:
        if not players:
            raise ValueError("At least one player is required.")
        self.players = players
        self.board = board or Board()
        self.dice_sides = dice_sides
        self._rng = rng or random.Random()
        self.turn_count = 0

    def roll_dice(self) -> int:
        """Roll the configured dice and return the result."""
        return self._rng.randint(1, self.dice_sides)

    def take_turn(self, player: Player) -> None:
        """Execute one turn for *player*."""
        if player.is_finished:
            return

        roll = self.roll_dice()
        player.move(roll, self.board.size)

        space = self.board.get_space(player.position)
        if space.space_type not in (SpaceType.START, SpaceType.FINISH):
            new_pos, soul_delta = space.apply(player.position)
            # Clamp boosted/penalised position to board bounds
            player.position = max(0, min(new_pos, self.board.size))
            if player.position >= self.board.size:
                player.is_finished = True
            player.apply_soul_delta(soul_delta)

    def play(self, max_turns: int = 500) -> GameResult:
        """Run a full game and return the result."""
        for player in self.players:
            player.reset()

        self.turn_count = 0
        winner = None

        while winner is None and self.turn_count < max_turns:
            for player in self.players:
                self.take_turn(player)
                if player.is_finished and winner is None:
                    winner = player.name
                    break
            self.turn_count += 1

        if winner is None:
            # Determine winner by position, then soul tokens
            best = max(
                self.players,
                key=lambda p: (p.position, p.soul_tokens),
            )
            winner = best.name

        return GameResult(
            winner=winner,
            turn_count=self.turn_count,
            final_positions={p.name: p.position for p in self.players},
            final_soul_tokens={p.name: p.soul_tokens for p in self.players},
        )
