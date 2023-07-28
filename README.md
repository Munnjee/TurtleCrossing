# Crossy Road in Python

This is a Python version of the classic Crossy Road game implemented using the Turtle graphics library. In this game, the player controls a turtle trying to cross a busy road filled with moving cars. The objective is to reach the other side safely while avoiding collisions with the cars.

### How to Play
1. Run the `main.py` file to start the game.
2. Use the **Up** arrow key to move the turtle up.
3. Use the **Down** arrow key to move the turtle down.
4. Cross the road without getting hit by any cars to advance to the next level.
5. If the turtle collides with a car, welp, GAME OVER.

### Requirements
- Python 3.x

### File Organization
- `main.py`: This file contains the main game loop and sets up the screen and objects.
- `player.py`: This file contains the `Player` class that represents the turtle controlled by the player.
- `car_manager.py`: This file contains the `CarManager` class responsible for creating and managing the moving cars.
- `scoreboard.py`: This file contains the `Scoreboard` class that keeps track of the player's score and level.

### How to Run
To play the game, ensure you have Python 3.x installed. Run the `main.py` file using the following command in your terminal or command prompt:

```
python main.py
```

### Gameplay
- The game window will open with a grid-like road and a turtle at the bottom.
- Use the **Up** and **Down** arrow keys to move the turtle up and down, respectively.
- Cross the road and reach the top of the screen to advance to the next level.
- Be careful to avoid collisions with the moving cars; if the turtle collides with any car, the game will end.
- The score and current level will be displayed at the top-left of the game window.
- Each successful crossing will increase the difficulty level, making the cars move faster.

### Disclaimer
This project is intended for educational purposes and entertainment only. The game is not affiliated with the official Crossy Road game, and no copyright infringement is intended.

Have fun playing Crossy Turtle!
