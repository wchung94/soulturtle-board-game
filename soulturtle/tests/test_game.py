"""Tests for the Game class."""

import random

import pytest

from soulturtle.board import Board, Space, SpaceType
from soulturtle.game import Game
from soulturtle.player import Player


def _make_game(num_players: int = 2, seed: int = 42) -> Game:
    players = [Player(name=f"P{i}") for i in range(num_players)]
    return Game(players=players, rng=random.Random(seed))


def test_game_requires_at_least_one_player() -> None:
    with pytest.raises(ValueError):
        Game(players=[])


def test_game_produces_a_winner() -> None:
    game = _make_game()
    result = game.play()
    assert result.winner in ("P0", "P1")


def test_game_turn_count_is_positive() -> None:
    game = _make_game()
    result = game.play()
    assert result.turn_count > 0


def test_game_single_player_always_wins() -> None:
    game = _make_game(num_players=1)
    result = game.play()
    assert result.winner == "P0"


def test_game_final_positions_present() -> None:
    game = _make_game()
    result = game.play()
    assert set(result.final_positions.keys()) == {"P0", "P1"}


def test_game_reset_between_plays() -> None:
    game = _make_game(seed=7)
    result1 = game.play()
    result2 = game.play()
    # Both runs should complete (determinism not required; just sanity check)
    assert result1.winner in ("P0", "P1")
    assert result2.winner in ("P0", "P1")


def test_roll_dice_in_range() -> None:
    game = _make_game()
    for _ in range(100):
        roll = game.roll_dice()
        assert 1 <= roll <= game.dice_sides
