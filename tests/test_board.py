"""Tests for the hexagonal board implementation."""

from src.components.board import Board, HexCoord, SpaceType


def test_generate_hex_board_returns_expected_unique_coordinates() -> None:
    sides = 4
    coords = Board._generate_hex_board(sides)

    assert len(coords) == 3 * sides * (sides - 1) + 1
    assert len(coords) == len(set(coords))
    assert all(max(abs(coord.q), abs(coord.r), abs(coord.q + coord.r)) <= sides - 1 for coord in coords)


def test_default_board_marks_six_corners_as_start_and_center_as_finish() -> None:
    board = Board(sides=5)
    start_spaces = [space for space in board._spaces if space.space_type == SpaceType.START]
    finish_spaces = [space for space in board._spaces if space.space_type == SpaceType.FINISH]

    assert len(start_spaces) == 6
    assert len(finish_spaces) == 1
    assert finish_spaces[0].hex_coord == HexCoord(0, 0)

    expected_corner_coords = {
        HexCoord(4, -4),
        HexCoord(4, 0),
        HexCoord(0, 4),
        HexCoord(-4, 4),
        HexCoord(-4, 0),
        HexCoord(0, -4),
    }
    assert {space.hex_coord for space in start_spaces} == expected_corner_coords


def test_action_spaces_have_effect_ids_in_expected_range() -> None:
    board = Board(sides=4)
    action_spaces = [space for space in board._spaces if space.space_type == SpaceType.ACTION]

    assert action_spaces
    assert all(space.effect > 0 for space in action_spaces)


def test_get_neighbors_returns_adjacent_hex_indices_for_center() -> None:
    board = Board(sides=3)
    center_index = next(
        space.index
        for space in board._spaces
        if space.hex_coord == HexCoord(0, 0)
    )

    neighbors = board.get_neighbors(center_index)
    neighbor_coords = {board.get_space(index).hex_coord for index in neighbors}

    assert len(neighbors) == 6
    assert neighbor_coords == {
        HexCoord(1, 0),
        HexCoord(-1, 0),
        HexCoord(0, 1),
        HexCoord(0, -1),
        HexCoord(1, -1),
        HexCoord(-1, 1),
    }


def test_get_neighbors_returns_three_neighbors_for_a_corner() -> None:
    board = Board(sides=4)
    corner_index = next(
        space.index
        for space in board._spaces
        if space.hex_coord == HexCoord(3, -3)
    )

    neighbors = board.get_neighbors(corner_index)
    neighbor_coords = {board.get_space(index).hex_coord for index in neighbors}

    assert len(neighbors) == 3
    assert neighbor_coords == {
        HexCoord(2, -3),
        HexCoord(3, -2),
        HexCoord(2, -2),
    }


def test_get_neighbors_returns_empty_list_for_invalid_index() -> None:
    board = Board(sides=3)

    assert board.get_neighbors(-1) == []
    assert board.get_neighbors(len(board._spaces)) == []
