"""Command-line entry point for the SoulTurtles simulator."""

from __future__ import annotations

import argparse

from .simulator import Simulator


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Monte Carlo simulation of SoulTurtles The Boardgame"
    )
    parser.add_argument(
        "players",
        nargs="+",
        metavar="PLAYER",
        help="Player names",
    )
    parser.add_argument(
        "-n",
        "--num-simulations",
        type=int,
        default=1000,
        metavar="N",
        help="Number of games to simulate (default: 1000)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        metavar="SEED",
        help="Random seed for reproducibility",
    )
    args = parser.parse_args()

    sim = Simulator(player_names=args.players, seed=args.seed)
    stats = sim.run(num_simulations=args.num_simulations)

    print(f"\nResults after {stats.num_simulations} simulations:\n")
    print(f"{'Player':<15} {'Wins':>6} {'Win Rate':>10} {'Avg Souls':>10}")
    print("-" * 45)
    for name in args.players:
        wins = stats.win_counts.get(name, 0)
        rate = stats.win_rates.get(name, 0.0)
        souls = stats.avg_soul_tokens.get(name, 0.0)
        print(f"{name:<15} {wins:>6} {rate:>10.1%} {souls:>10.2f}")
    print(f"\nAverage turns per game: {stats.avg_turn_count:.1f}")


if __name__ == "__main__":
    main()
