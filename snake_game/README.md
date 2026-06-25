# Snake Game 🐍

A classic Snake game implementation using Python's Turtle graphics library.

## Description

This is a simple yet entertaining Snake game where you control a snake to eat food and grow longer. The game ends when the snake collides with the wall or its own tail.

## Features

- **Classic Snake Gameplay**: Control the snake using arrow keys
- **Score Tracking**: Keep track of your score as you eat food
- **Collision Detection**: Game ends on wall or self-collision
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
3. Avoid hitting the walls (game boundaries)
4. Avoid colliding with your own tail
5. The game ends when you hit a wall or your tail

## Project Structure

```
snake_game/
├── main.py          # Main game loop and setup
├── snake.py         # Snake class with movement logic
├── food.py          # Food class for random food placement
├── scoreboard.py    # Scoreboard class for score tracking
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Code Overview

### main.py
- Sets up the game screen (600x600 pixels, black background)
- Initializes snake, food, and scoreboard objects
- Contains the main game loop
- Handles collision detection (food, walls, tail)
- Manages keyboard input

### snake.py
- `Snake` class manages the snake's segments
- Handles snake movement and direction changes
- Implements snake extension when food is eaten
- Prevents 180-degree turns

### food.py
- `Food` class inherits from Turtle
- Randomly places food on the screen
- Refreshes food position when eaten

### scoreboard.py
- `Scoreboard` class displays current score
- Updates score when food is eaten
- Shows "Game Over" message when game ends

## Game Configuration

You can modify these constants in the respective files:

**snake.py:**
- `MOVE_DISTANCE = 20`: Distance snake moves per step
- `STARTING_POSITIONS`: Initial snake segment positions

**main.py:**
- `screen.setup(width=600, height=600)`: Game window size
- `time.sleep(0.2)`: Game speed (lower = faster)
- Collision distances for food (15) and tail (10)

## Future Enhancements

Potential improvements:
- [ ] Add high score tracking with file persistence
- [ ] Implement difficulty levels (speed variations)
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
- **Solution**: Adjust `time.sleep()` value in main.py (line 28)

**Issue**: Controls not responding
- **Solution**: Click on the game window to ensure it has focus

## License

This is a learning project and is free to use for educational purposes.

## Author

Created as part of Python learning exercises.

---

Enjoy the game! 🎮