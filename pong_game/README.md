# Pong Game 🏓

A classic two-player Pong game built with Python's Turtle graphics library.

## Description

This is a two-player Pong game where each player controls a paddle to keep the ball in play. The first player to reach **5 points** wins the game.

## Features

- **Two-Player Gameplay**: Both players share the same keyboard
- **Score Tracking**: Live score display at the top of the screen
- **Ball Speed**: Ball accelerates slightly with each paddle hit
- **Colour-Coded Paddles**: Hot-pink (left) and electric-blue (right)
- **Win Condition**: First to 5 points wins; "Game Over" message displayed

## Requirements

- Python 3.6 or higher
- Turtle graphics library (included in Python standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `pong_game` directory:
   ```bash
   cd python-learning/pong_game
   ```

## How to Run

```bash
python3 main.py
```

## Controls

| Action            | Left Player | Right Player |
|-------------------|-------------|--------------|
| Move paddle up    | `Left` ←   | `Up` ↑       |
| Move paddle down  | `Right` →  | `Down` ↓     |

> **Note:** Click the game window first to ensure it has keyboard focus.

## Game Rules

1. The ball starts at the centre and moves diagonally.
2. Hit the ball with your paddle to send it back.
3. Each time the ball passes your opponent's paddle, you score a point.
4. The ball resets to the centre after every point.
5. The first player to reach **5 points** wins.

## Project Structure

```
pong_game/
├── main.py          # Game setup, main loop, collision detection
├── paddle.py        # Paddle class with up/down movement
├── ball.py          # Ball class with movement and bounce logic
├── scoreboard.py    # Scoreboard class for live score and game-over display
├── requirements.txt # Dependency notes (standard library only)
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Code Overview

### `main.py`
- Sets up the game screen (800 × 600 pixels, black background)
- Binds keyboard controls to the left and right paddles
- Runs the main game loop: moves ball, detects collisions, updates score
- Ends the game when a player reaches `WINING_SCORE = 5`

### `paddle.py`
- `Paddle(color, position)` — creates a coloured, vertical paddle at a given position
- `go_up()` / `go_down()` — moves the paddle 20 units per key press

### `ball.py`
- `Ball` inherits from `Turtle`; starts at the centre moving diagonally
- `move()` — advances ball by `x_move`/`y_move` each tick
- `bounce_y()` — reverses vertical direction on wall hit
- `bounce_x()` — reverses horizontal direction on paddle hit; speeds ball up by 10 %
- `reset_position()` — returns ball to centre and resets speed after a point

### `scoreboard.py`
- `Scoreboard` displays left and right scores at the top of the screen
- `l_pont()` / `r_pont()` — increment respective score and refresh display
- `game_over()` — writes "Game Over" at the centre of the screen

## Configuration

Modify these constants in `main.py` to customise the game:

| Constant            | Default       | Effect                          |
|---------------------|---------------|---------------------------------|
| `SCREEN_WIDTH`      | `800`         | Window width in pixels          |
| `SCREEN_HEIGHT`     | `600`         | Window height in pixels         |
| `WINING_SCORE`      | `5`           | Points needed to win            |
| `LEFT_PADDLE_COLOR` | Hot pink      | RGB colour of left paddle       |
| `RIGHT_PADDLE_COLOR`| Electric blue | RGB colour of right paddle      |

Modify `ball.py` to tune ball behaviour:

| Attribute     | Default | Effect                                      |
|---------------|---------|---------------------------------------------|
| `x_move`      | `10`    | Horizontal speed per tick                   |
| `y_move`      | `10`    | Vertical speed per tick                     |
| `move_speed`  | `0.1`   | Delay (seconds) per frame; lower = faster   |

## Future Enhancements

- [ ] Add boundary limits to stop paddles from leaving the screen
- [ ] Implement a serve mechanic (random initial ball direction)
- [ ] Add sound effects on bounce and point
- [ ] Support a single-player mode against a simple AI
- [ ] Persist and display a high-score leaderboard
- [ ] Add a pause / resume feature

## Learning Objectives

This project demonstrates:
- Object-Oriented Programming (OOP) with class inheritance
- Game loop design and frame-rate control
- Keyboard event handling with Turtle
- Collision detection (wall, paddle, boundary)
- RGB colour mode in Turtle (`colormode(255)`)

## Troubleshooting

**Game window doesn't appear**
→ Ensure Python 3 is installed with Tkinter/Turtle support.

**Controls not responding**
→ Click the game window to give it keyboard focus.

**Ball moves too fast or too slow**
→ Adjust `move_speed` in `ball.py` (higher value = slower).

## License

This is a learning project and is free to use for educational purposes.

## Author

Created as part of Python learning exercises.

---

Enjoy the game! 🎮
