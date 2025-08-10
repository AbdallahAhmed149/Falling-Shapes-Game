# Falling Shapes Game 🎮✨

Welcome to **Falling Shapes Game**, a fun and addictive Python-based game built using the Turtle graphics library! 🐢 Catch colorful shapes falling from the sky, score points, and avoid the dreaded white turtle to keep the game going! 🚀

## Game Overview 📜
In this game, you control a white rectangular "bowl" at the bottom of the screen using the **Left** and **Right** arrow keys. Various shapes (circles, squares, turtles, and triangles) fall from the top of the screen, each with a random color and size. Your goal is to catch these shapes to earn points while avoiding the game-ending white turtle! ☠️

### Scoring System 🥗
- **Square**: +2 points 🟦
- **Circle**: +1 point 🔴
- **Colored Turtle**: +5 points 🐢
- **Triangle**: Resets your score to 0 ⚠️
- **White Turtle**: Ends the game 😵

Win the game by reaching a score of **50** or more! 🎉

## How to Play 🕹️
1. Use the **Left Arrow** ⬅️ and **Right Arrow** ➡️ keys to move the bowl.
2. Catch falling shapes to increase your score.
3. Avoid the white turtle at all costs—it ends the game!
4. Reach 50 points to win and celebrate your victory! 🏆

## Installation ⚙️
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/falling-shapes-game.git
   ```
2. Ensure you have Python installed (version 3.6 or higher).
3. No additional libraries are required since the game uses Python's built-in `turtle` module.
4. Run the game by executing:
   ```bash
   python main.py
   ```

## Files 📂
- `main.py`: The main game loop and logic.
- `bowl.py`: Defines the player-controlled bowl.
- `shapes.py`: Manages the falling shapes with random properties.
- `score.py`: Handles the scoreboard display.
- `main.spec`: PyInstaller configuration for packaging the game into an executable.

## Building the Executable 📦
To create a standalone executable for the game:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the following command in the project directory:
   ```bash
   pyinstaller main.spec
   ```
3. Find the executable in the `dist` folder.

## Requirements 🛠️
- Python 3.6+
- PyInstaller (optional, for building the executable)

## Why Play? 🤗
This game is a simple yet engaging way to test your reflexes and have fun with Python's Turtle graphics. Perfect for beginners learning Python or anyone looking for a quick gaming break! 😄

## Contributing 🤝
Feel free to fork this repository, make improvements, and submit pull requests. Ideas for new features, bug fixes, or optimizations are always welcome! 🌟

## License 📝
This project is licensed under the MIT License. See the `LICENSE` file for details.

Happy gaming, and may you catch all the shapes! 🎯
