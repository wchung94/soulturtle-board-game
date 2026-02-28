"""Monte Carlo simulator for SoulTurtles."""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field

from .board import Board
from .game import Game, GameResult
from .player import Player


@dataclass
class SimulationStats:
    """Aggregated statistics from many simulated games."""

    num_simulations: int
    win_counts: dict[str, int] = field(default_factory=dict)
    avg_turn_count: float = 0.0
    avg_soul_tokens: dict[str, float] = field(default_factory=dict)

    @property
    def win_rates(self) -> dict[str, float]:
        """Return win rate for each player."""
        return {
            name: count / self.num_simulations
            for name, count in self.win_counts.items()
        }


class Simulator:
    """Runs Monte Carlo simulations of SoulTurtles games."""

    def __init__(
        self,
        player_names: list[str],
        board: Board | None = None,
        dice_sides: int = 6,
        seed: int | None = None,
    ) -> None:
        if not player_names:
            raise ValueError("At least one player name is required.")
        self.player_names = player_names
        self.board = board or Board()
        self.dice_sides = dice_sides
        self._rng = random.Random(seed)

    def run(self, num_simulations: int = 1000) -> SimulationStats:
        """Simulate *num_simulations* games and return aggregated stats."""
        win_counts: Counter[str] = Counter()
        total_turns = 0
        soul_token_totals: dict[str, int] = {n: 0 for n in self.player_names}

        for _ in range(num_simulations):
            players = [Player(name=n) for n in self.player_names]
            game = Game(
                players=players,
                board=self.board,
                dice_sides=self.dice_sides,
                rng=self._rng,
            )
            result: GameResult = game.play()
            win_counts[result.winner] += 1
            total_turns += result.turn_count
            for name in self.player_names:
                soul_token_totals[name] += result.final_soul_tokens.get(name, 0)

        return SimulationStats(
            num_simulations=num_simulations,
            win_counts=dict(win_counts),
            avg_turn_count=total_turns / num_simulations,
            avg_soul_tokens={
                name: soul_token_totals[name] / num_simulations
                for name in self.player_names
            },
        )
