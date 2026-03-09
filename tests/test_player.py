"""Tests for the Player class."""

from soulturtle.player import Player


def test_player_initial_state() -> None:
    player = Player(name="Alice")
    assert player.position == 0
    assert player.soul_tokens == 0
    assert not player.is_finished


def test_player_move_advances_position() -> None:
    player = Player(name="Alice")
    player.move(5, board_size=30)
    assert player.position == 5
    assert not player.is_finished


def test_player_move_caps_at_board_size() -> None:
    player = Player(name="Alice", position=28)
    player.move(5, board_size=30)
    assert player.position == 30
    assert player.is_finished


def test_player_move_exact_finish() -> None:
    player = Player(name="Alice", position=25)
    player.move(5, board_size=30)
    assert player.position == 30
    assert player.is_finished


def test_player_apply_soul_delta_positive() -> None:
    player = Player(name="Alice", soul_tokens=3)
    player.apply_soul_delta(2)
    assert player.soul_tokens == 5


def test_player_apply_soul_delta_negative() -> None:
    player = Player(name="Alice", soul_tokens=3)
    player.apply_soul_delta(-2)
    assert player.soul_tokens == 1


def test_player_soul_tokens_floor_at_zero() -> None:
    player = Player(name="Alice", soul_tokens=1)
    player.apply_soul_delta(-10)
    assert player.soul_tokens == 0


def test_player_reset() -> None:
    player = Player(name="Alice", position=20, soul_tokens=5, is_finished=True)
    player.reset()
    assert player.position == 0
    assert player.soul_tokens == 0
    assert not player.is_finished
