# Battle commander

More about the game: [Battleship](https://en.wikipedia.org/wiki/Battleship_%28game%29).

Requirements:

Python 3.x

**Recommended**:
- Unix like environment

Instructions:

Run
```bash
./app.py
```

Sample output:
```
Let's play Battleship!
  1 2 3 4 5 6 7 8 9 10 
A . . . . . . . . . .
B . . . . . . . . . .
C . . . . . . . . . .
D . . . . . . . . . .
E . . . . . . . . . .
F . . . . . . . . . .
G . . . . . . . . . .
H . . . . . . . . . .
I . . . . . . . . . .
J . . . . . . . . . .
> help
Usage:
cheat - Reveal enemy's ships.
exit - Exit from the app.
help - App usage (this menu).
restart - Restart the game.
> A1
```

### Features

- Board manager
  * Render board
  * 3 different icons:
    cloaked ship part, ghost ship part and hit ship part
  * Labels customizable, can hidden by config 
- Game manager
  * Manages game loop
  * Counts available moves
  * Game over option
- Menu
  * Manages menu driven shell
  * Help included
- Player
  * Parses input coordinates
  * Validates coordinates
- Commands
 * Cheat, allows to draw the ship parts with ghost like icon - for debug
 * Exit, exits the program
 * Restart, starts the game from start
