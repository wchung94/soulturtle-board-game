# soulturtle-board-game
Monte Carlo simulation of SoulTurtles The Boardgame to find the optimal parameters for balanced game.

## Rules

### Core
Game Concept: “SoulTurle: Board Game”

Players begin on one of the six outer corners of a giant hexagonal board composed of smaller hex tiles. Their goal is to reach the central hex first. Every tile they step on triggers a card draw from one of three decks, creating a dynamic mix of strategy, risk, and chaos.
### Board Layout

    The board is a large hexagon made of concentric rings of smaller hex tiles.

    The number of rings can scale with player count:

        3 players: 4 rings

        4–5 players: 5 rings

        6 players: 6 rings

    Each ring contains tiles of different types (color-coded):

        Path tiles (common)

        Challenge tiles

        Resource tiles

        Wild tiles (rare, unpredictable)

Players start on any of the six corner tiles (one per corner; if more than six players, two can share a corner).

### Turn Structure

On your turn:

    Roll a movement die (1–3 steps).

    Move in any direction toward the center, but you cannot backtrack in the same turn.

    When you land on a tile, draw the corresponding card type.

Three Card Types

Each tile color corresponds to one of the three decks.
1. Event Cards (from Path tiles)

These create immediate effects.
Examples:

    “Sudden Storm: Move back 1 tile.”

    “Shortcut: Move 2 tiles toward the center.”

    “Lost Map: Skip your next turn.”

2. Location Cards (from Location tiles)

These require a roll or choice.
Examples:

    “Cross the Ravine: Roll 4–6 to succeed. Success: Move forward 1. Fail: Move sideways to nearest tile.”

    “Duel: Choose a player. Both roll. Winner steals a resource.”

3. Entity Cards (from Entity tiles)

These are kept in hand and used strategically.
Examples:

    “Bridge Plank: Ignore the next Challenge card.”

    “Compass: Reroll any movement die.”

    “Warp Crystal: Teleport to any tile in the next inner ring.”

### Winning the Game

The first player to reach the center tile must draw one final Event card.
If the card is beneficial or neutral, they win.
If it’s negative, they are pushed back and must try again.

This creates tension and prevents anticlimactic endings.

#### Player Interaction

To keep things lively:

    Some Event cards affect all players.

    Some Challenge cards let you target others.

    Resource cards can be traded (optional rule).

### Optional Variants
1. Cooperative Mode

Players must all reach the center before a “Doom Tracker” fills up.
2. Saboteur Mode

One player is secretly trying to prevent others from reaching the center.
3. Modular Board

Shuffle hex tiles each game for a new layout.

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
