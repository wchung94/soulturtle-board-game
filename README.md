# soulturtle-board-game
Monte Carlo simulation of SoulTurtles The Boardgame

## Project structure

```
soulturtle/
  src/
    components/
      board.py      – Board and Space definitions
      player.py     – Player model
      game.py       – Game engine (single play-through)
      simulator.py  – Monte Carlo simulator (many games)
      __main__.py   – CLI entry point
  tests/
    test_board.py
    test_player.py
    test_game.py
    test_simulator.py
```

## Installation

```bash
pip install -e .
```

## Usage

### Run a simulation from the command line

```bash
python -m soulturtle Milan Rody Wing --num-simulations 1000 --seed 42
```

```
Results after 1000 simulations:

Player            Wins   Win Rate  Avg Souls
---------------------------------------------
Alice              413      41.3%       0.00
Bob                328      32.8%       0.00
Carol              259      25.9%       0.00

Average turns per game: 6.7
```

### Use the Python API

```python
from soulturtle import Simulator

sim = Simulator(player_names=["Alice", "Bob"], seed=0)
stats = sim.run(num_simulations=10_000)

print(stats.win_rates)      # {'Alice': 0.573, 'Bob': 0.427}
print(stats.avg_turn_count) # ~6.8
```

## Running tests

```bash
pip install pytest
pytest
```
