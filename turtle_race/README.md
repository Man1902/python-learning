# Turtle Race 🐢

A colourful betting game where six turtles race across the screen, built with Python's Turtle graphics library.

## Description

Six turtles — each a different colour — race from the left edge to the right edge of the screen. Before the race begins you place a bet by typing the colour of the turtle you think will win. Each turtle advances a random distance every tick, so every race has a different outcome.

## Features

- **Colour Betting**: Enter your colour pick before the race starts via a pop-up dialog
- **Randomised Movement**: Each turtle moves a random 0–10 units per tick — no two races are the same
- **Six Competitors**: Red, Orange, Yellow, Green, Blue, Purple
- **Instant Result**: Prints win/loss result to the console when a turtle crosses the finish line

## Requirements

- Python 3.9 or higher (uses built-in `list[Turtle]` type hint)
- `turtle`, `random`, and `time` modules (all included in Python's standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `turtle_race` directory:
   ```bash
   cd python-learning/turtle_race
   ```

## How to Run

```bash
python3 main.py
```

A dialog box will appear asking you to choose a colour. Type one of the colours listed and press **OK** to start the race.

## How to Play

1. A pop-up prompt appears: `"Which turtle will win the race? Enter a color from [...]"`
2. Type one of the six colours (e.g. `blue`) and click **OK**
3. Watch the race — turtles move simultaneously, each a random distance per frame
4. The first turtle to reach the right edge wins
5. The result is printed to your terminal:
   - **Win** → `"You've won! The <color> turtle is the winner!"`
   - **Loss** → `"You've lost! The <color> turtle is the winner!"`
6. Click the window to close it

## Turtle Colours

| Colour | Starting Y position |
|--------|---------------------|
| Red    | -70                 |
| Orange | -40                 |
| Yellow | -10                 |
| Green  |  20                 |
| Blue   |  50                 |
| Purple |  80                 |

All turtles start at x = -380 and finish at x = 375 (on an 800 × 500 screen).

## Project Structure

```
turtle_race/
├── main.py          # All game logic — setup, race loop, result detection
├── requirements.txt # Dependency notes (standard library only)
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Code Overview

### `main.py`

| Section | Description |
|---------|-------------|
| Constants | `COLORS` list, `X_POSITION` (finish line offset), `Y_POSITIONS` (lane offsets) |
| Screen setup | 800 × 500 window, no auto-render (`tracer(0)`) |
| Bet input | `screen.textinput()` pop-up collects the player's colour bet |
| Turtle creation | Loop builds 6 `Turtle` objects, colours them, and places each in its lane |
| Race loop | Each tick: `screen.update()`, random forward move per turtle, finish-line check |
| Result | Compares winning turtle's `pencolor()` against `user_bet`; prints outcome |

## Configuration

Modify these values in [`main.py`](main.py) to customise the game:

| Constant       | Default                                           | Effect                              |
|----------------|---------------------------------------------------|-------------------------------------|
| `COLORS`       | `["red","orange","yellow","green","blue","purple"]` | Turtle colours and bet options    |
| `X_POSITION`   | `380`                                             | Distance from centre to start/finish|
| `Y_POSITIONS`  | `[-70,-40,-10,20,50,80]`                          | Vertical lane positions             |
| `time.sleep()` | `0.1`                                             | Frame delay — lower = faster race   |
| `randint(0,10)`| `0–10`                                            | Random step range per turtle/tick   |

## Future Enhancements

- [ ] Show the winner's colour on-screen (not just in the terminal)
- [ ] Allow the player to replay without restarting the script
- [ ] Display each turtle's colour label next to its lane
- [ ] Track win/loss statistics across multiple races
- [ ] Add a countdown before the race begins
- [ ] Support a configurable number of turtles

## Learning Objectives

This project demonstrates:
- Using `turtle` for graphics and user input (`textinput`)
- Randomised simulation with the `random` module
- List comprehension and `for` loop iteration over objects
- Game loop design with `tracer(0)` + `screen.update()` for manual rendering
- Basic type hints (`list[Turtle]`)

## Troubleshooting

**Bet dialog does not appear**
→ The Turtle window may be hidden behind other windows — check your taskbar.

**Pressing Cancel or leaving the input blank**
→ The race will not start (the `if user_bet:` guard prevents it). Re-run the script.

**Game window does not close**
→ Click anywhere on the window to exit (`screen.exitonclick()`).

**Race is too fast or too slow**
→ Adjust `time.sleep(0.1)` or the `randint(0, 10)` range in `main.py`.

## License

This is a learning project and is free to use for educational purposes.

## Author

Created as part of Python learning exercises.

---

Good luck with your bet! 🎲
