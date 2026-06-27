# Snake Game 🐍

A classic Snake game implementation using Python's Turtle graphics library.

## Description

This is a simple yet entertaining Snake game where you control a snake to eat food and grow longer. When the snake collides with the wall or its own tail, the score resets and the game continues — your **high score is saved automatically** between rounds.

## Features

- **Classic Snake Gameplay**: Control the snake using arrow keys
- **Score Tracking**: Keep track of your current score as you eat food
- **Persistent High Score**: Best score is saved to `data.txt` and shown on screen across rounds
- **Progressive Speed**: Snake gets faster with every food eaten (speed increases by 10% per food)
- **Collision Handling**: On wall or tail collision the snake resets and the game continues — no hard game-over
- **Growing Snake**: Snake extends each time it eats food
- **Smooth Animation**: Clean graphics using Turtle module

## Requirements

- Python 3.6 or higher
- Turtle graphics library (included in Python standard library)

## Installation

1. Clone or download this repository
2. Navigate to the snake_game directory:
   ```bash
   cd python-learning/snake_game
   ```

## How to Run

Simply run the main.py file:

```bash
python3 main.py
```

## How to Play

- **Up Arrow**: Move snake up
- **Down Arrow**: Move snake down
- **Left Arrow**: Move snake left
- **Right Arrow**: Move snake right

### Game Rules

1. Use arrow keys to control the snake's direction
2. Eat the red food to grow longer and increase your score
3. Each food eaten makes the snake move 10% faster — the challenge ramps up!
4. Avoid hitting the walls (game boundaries)
5. Avoid colliding with your own tail
6. On a collision, the snake resets and a new round begins automatically — your high score is preserved

## Project Structure

```
snake_game/
├── main.py          # Main game loop and setup
├── snake.py         # Snake class with movement logic
├── food.py          # Food class for random food placement
├── scoreboard.py    # Scoreboard class for score tracking
├── data.txt         # Persisted high score (auto-updated at runtime)
├── requirements.txt # Python dependencies
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Code Overview

### main.py
- Sets up the game screen (600×600 pixels, black background)
- Initialises snake, food, and scoreboard objects
- Contains the main game loop with a variable `move_speed` (starts at `0.2` s)
- On each food collision: extends snake, increments score, refreshes food, and reduces `move_speed` by 10% (`move_speed *= 0.9`)
- Handles collision detection (food at distance < 15, walls at ±280, tail at distance < 10)
- Manages keyboard input


### food.py
- `Food` class inherits from Turtle
- Randomly places food on the screen
- Refreshes food position when eaten

### scoreboard.py
- `Scoreboard` class displays current score and high score at position `(0, 260)` — format: `Score: X   High Score: Y`
- Reads the persisted high score from `data.txt` on initialisation
- `increase_score()` increments score and redraws the scoreboard
- `reset()` checks if the current score beats the high score, writes the new high score to `data.txt` if so, then resets the current score to `0` and redraws — no game-over screen

### snake.py
- `Snake` class manages the snake's segments
- Handles snake movement and direction changes
- `extend()` appends a new segment at the tail position when food is eaten
- `reset()` teleports all existing segments off-screen, clears the list, and re-creates the snake at the starting positions — used to restart after a collision
- Prevents 180-degree turns (can't reverse direction directly)

## Game Configuration

You can modify these values in the respective files:

**`main.py`:**

| Value | Default | Effect |
|-------|---------|--------|
| `move_speed` | `0.2` | Initial frame delay in seconds — lower is faster |
| `move_speed *= 0.9` | `0.9` multiplier | Speed-up factor per food eaten — lower multiplier = faster ramp |
| `screen.setup(width=600, height=600)` | 600×600 | Game window size |
| Food collision distance | `15` | How close the head must be to eat food |
| Tail collision distance | `10` | How close the head triggers a tail collision |

**`snake.py`:**

| Constant | Default | Effect |
|----------|---------|--------|
| `MOVE_DISTANCE` | `20` | Pixels the snake moves per step |
| `STARTING_POSITIONS` | 3 segments at origin | Initial snake length and position |

## Future Enhancements

Potential improvements:
- [x] ~~Add high score tracking with file persistence~~ — done: high score saved to `data.txt`
- [x] ~~Implement difficulty levels (speed variations)~~ — done: speed increases 10% per food
- [x] ~~Game continuation after collision~~ — done: snake resets and game resumes automatically
- [ ] Add sound effects
- [ ] Create a pause/resume feature
- [ ] Add obstacles or power-ups
- [ ] Implement a menu system

## Learning Objectives

This project demonstrates:
- Object-Oriented Programming (OOP) in Python
- Game loop implementation
- Event handling (keyboard input)
- Collision detection
- Turtle graphics module usage
- Class inheritance

## Troubleshooting

**Issue**: Game window doesn't appear
- **Solution**: Ensure Python 3 is installed and Turtle module is available

**Issue**: Game is too fast/slow
- **Solution**: Adjust `move_speed` (initial value) in `main.py`; or change the `0.9` multiplier to slow down the speed progression (higher = slower ramp-up)

**Issue**: Controls not responding
- **Solution**: Click on the game window to ensure it has focus

## License

This is a learning project and is free to use for educational purposes.

## Author

Created as part of Python learning exercises.

---

Enjoy the game! 🎮