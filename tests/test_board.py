"""Tests for the Board and Space classes."""

import pytest

from soulturtle.board import Board, Space, SpaceType


def test_default_board_size() -> None:
    board = Board()
    assert board.size == 30


def test_first_space_is_start() -> None:
    board = Board()
    assert board.get_space(0).space_type == SpaceType.START


def test_last_space_is_finish() -> None:
    board = Board()
    assert board.get_space(30).space_type == SpaceType.FINISH


def test_get_space_clamps_to_finish() -> None:
    board = Board()
    space = board.get_space(9999)
    assert space.space_type == SpaceType.FINISH


def test_boost_space_moves_player_forward() -> None:
    space = Space(index=5, space_type=SpaceType.BOOST, effect=3)
    new_pos, soul_delta = space.apply(5)
    assert new_pos == 8
    assert soul_delta == 0


def test_penalty_space_moves_player_back() -> None:
    space = Space(index=10, space_type=SpaceType.PENALTY, effect=2)
    new_pos, soul_delta = space.apply(10)
    assert new_pos == 8
    assert soul_delta == 0


def test_penalty_space_does_not_go_below_zero() -> None:
    space = Space(index=1, space_type=SpaceType.PENALTY, effect=5)
    new_pos, _ = space.apply(1)
    assert new_pos == 0


def test_warp_space_teleports_player() -> None:
    space = Space(index=8, space_type=SpaceType.WARP, warp_target=18)
    new_pos, _ = space.apply(8)
    assert new_pos == 18


def test_normal_space_returns_soul_delta() -> None:
    space = Space(index=3, space_type=SpaceType.NORMAL, effect=2)
    new_pos, soul_delta = space.apply(3)
    assert new_pos == 3
    assert soul_delta == 2


def test_custom_board() -> None:
    spaces = [Space(i) for i in range(6)]
    spaces[5].space_type = SpaceType.FINISH
    board = Board(spaces=spaces)
    assert board.size == 5
