# Turtle Road Crossing 🐢🚗

A Frogger-inspired road crossing game built with Python's Turtle graphics library.

## Description

Guide a red turtle from the bottom of the screen to the finish line at the top while dodging an endless stream of coloured cars. Every successful crossing advances the level — and makes the cars faster.

## Features

- **Dodge the Traffic**: Avoid randomly generated cars moving from right to left
- **Progressive Difficulty**: Cars speed up by 10 units every time you cross (`MOVE_INCREMENT = 10`)
- **Level Tracking**: Current level displayed live in the top-left corner
- **Collision Detection**: Game ends immediately if a car hits the player
- **Auto-Reset**: Player returns to the start after each successful crossing

## Requirements

- Python 3.6 or higher
- `turtle`, `random`, and `time` modules (all included in Python's standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `turtle_road_crossing` directory:
   ```bash
   cd python-learning/turtle_road_crossing
   ```

## How to Run

```bash
python3 main.py
```

## Controls

| Key | Action |
|-----|--------|
| `Up` ↑ | Move turtle forward (upward) |

## Game Rules

1. Press the **Up** arrow key to move the turtle toward the finish line
2. Avoid all cars — any collision ends the game immediately
3. Reach the top of the screen (y > 280) to complete a crossing
4. Each successful crossing increases the level and car speed
5. The game ends when a car hits the turtle; "Game Over" is shown on screen

## Project Structure

```
turtle_road_crossing/
├── main.py          # Game setup, main loop, collision and crossing detection
├── player.py        # Player (turtle) class with movement and finish-line logic
├── car_manager.py   # CarManager class — spawning, moving, and levelling up cars
├── scoreboard.py    # Scoreboard class — live level display and game-over message
├── requirements.txt # Dependency notes (standard library only)
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Code Overview

### `main.py`
- Sets up a 600 × 600 screen with the title "Turtle Road Crossing"
- Binds the `Up` key to `player.go_up()`
- Main loop (0.1 s tick):
  - Spawns and moves cars via `CarManager`
  - Checks player–car distance (< 20) → game over
  - Checks if player reached the finish line → reset player, level up cars and scoreboard

### `player.py`
- `Player` inherits from `Turtle`; starts at `(0, -280)`, facing up
- `go_up()` — moves the turtle 10 units forward per key press
- `go_to_start()` — resets position to `(0, -280)`
- `is_at_finish_line()` — returns `True` when `ycor() > 280`

### `car_manager.py`
- `CarManager` maintains `all_cars` list and a `car_speed` counter
- `create_car()` — 1-in-6 chance each tick of spawning a random-coloured car at x = 300
- `move_cars()` — moves every car backward by `car_speed` units
- `level_up()` — increments `car_speed` by `MOVE_INCREMENT` (10) on each crossing

### `scoreboard.py`
- `Scoreboard` inherits from `Turtle`; positioned at `(-280, 260)`
- `update_scoreboard()` — clears and rewrites `"Level N"` in Courier 24
- `increase_level()` — increments level and refreshes the display
- `game_over()` — writes "Game Over" at the centre of the screen

## Configuration

Modify these values to customise the game:

**`car_manager.py`:**

| Constant | Default | Effect |
|----------|---------|--------|
| `START_MOVE_DISTANCE` | `5` | Initial car speed (pixels per tick) |
| `MOVE_INCREMENT` | `10` | Speed added per level |
| `COLORS` | 6 colours | Pool of random car colours |

**`player.py`:**

| Constant | Default | Effect |
|----------|---------|--------|
| `START_POSITION` | `(0, -280)` | Player starting position |
| `MOVE_DISTANCE` | `10` | Pixels moved per key press |
| `FINISH_LINE_Y` | `280` | Y coordinate that counts as a crossing |

**`main.py`:**

| Value | Default | Effect |
|-------|---------|--------|
| `time.sleep(0.1)` | `0.1` s | Frame delay — lower = faster game tick |
| Car collision distance | `20` | Distance threshold for a car hit |
| `screen.setup(...)` | 600 × 600 | Window size |

## Future Enhancements

- [ ] Add boundary lanes so cars only spawn on the road area
- [ ] Display a high-score / max level reached
- [ ] Add multiple player lives before game over
- [ ] Show a countdown before the game starts
- [ ] Add sound effects on collision or level-up
- [ ] Support left/right movement for finer navigation

## Learning Objectives

This project demonstrates:
- Object-Oriented Programming with class inheritance (`Turtle` subclassing)
- Game loop design with `tracer(0)` + `screen.update()` for manual rendering
- Random event spawning (1-in-6 car creation chance)
- Collision detection via Turtle's `distance()` method
- Progressive difficulty through a mutable speed variable

## Troubleshooting

**Game window doesn't appear**
→ Ensure Python 3 is installed with Tkinter/Turtle support.

**Controls not responding**
→ Click the game window to give it keyboard focus.

**Cars are too fast from the start**
→ Lower `START_MOVE_DISTANCE` in `car_manager.py`.

**Speed ramp feels too steep**
→ Lower `MOVE_INCREMENT` in `car_manager.py` (e.g. `5` instead of `10`).

## License

This is a learning project and is free to use for educational purposes.

## Author

Created as part of Python learning exercises.

---

Good luck crossing the road! 🚦
