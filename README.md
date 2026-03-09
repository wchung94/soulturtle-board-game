# soulturtle-board-game
Monte Carlo simulation of SoulTurtles The Boardgame to find the optimal parameters for balanced game.

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
uv run python -m soulturtle
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
Wing              413      41.3%       0.00
Milan             328      32.8%       0.00
Rody              259      25.9%       0.00

Average turns per game: 6.7
```

### Use the Python API

```python
from soulturtle import Simulator

sim = Simulator(player_names=["Milan", "Rody"], seed=0)
stats = sim.run(num_simulations=10_000)

print(stats.win_rates)      # {'Milan': 0.573, 'Rody': 0.427}
print(stats.avg_turn_count) # ~6.8
```

## Running tests

```bash
pip install pytest
pytest
```
