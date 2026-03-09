"""Tests for the Monte Carlo Simulator."""

import pytest

from soulturtle.simulator import Simulator, SimulationStats


def test_simulator_requires_players() -> None:
    with pytest.raises(ValueError):
        Simulator(player_names=[])


def test_simulation_returns_stats() -> None:
    sim = Simulator(player_names=["Alice", "Bob"], seed=0)
    stats = sim.run(num_simulations=100)
    assert isinstance(stats, SimulationStats)


def test_simulation_count_matches() -> None:
    sim = Simulator(player_names=["Alice", "Bob"], seed=1)
    stats = sim.run(num_simulations=200)
    assert stats.num_simulations == 200


def test_win_counts_sum_to_simulations() -> None:
    sim = Simulator(player_names=["Alice", "Bob"], seed=2)
    stats = sim.run(num_simulations=100)
    assert sum(stats.win_counts.values()) == 100


def test_win_rates_sum_to_one() -> None:
    sim = Simulator(player_names=["Alice", "Bob"], seed=3)
    stats = sim.run(num_simulations=100)
    total = sum(stats.win_rates.values())
    assert abs(total - 1.0) < 1e-9


def test_avg_turn_count_is_positive() -> None:
    sim = Simulator(player_names=["Alice", "Bob"], seed=4)
    stats = sim.run(num_simulations=50)
    assert stats.avg_turn_count > 0


def test_avg_soul_tokens_keys_match_players() -> None:
    names = ["Alice", "Bob", "Carol"]
    sim = Simulator(player_names=names, seed=5)
    stats = sim.run(num_simulations=50)
    assert set(stats.avg_soul_tokens.keys()) == set(names)


def test_simulation_is_reproducible() -> None:
    sim1 = Simulator(player_names=["Alice", "Bob"], seed=99)
    sim2 = Simulator(player_names=["Alice", "Bob"], seed=99)
    stats1 = sim1.run(num_simulations=100)
    stats2 = sim2.run(num_simulations=100)
    assert stats1.win_counts == stats2.win_counts
