# Connect4Game 

## Overview
This is a simple implementation of the classic **Connect 4** game using Python. Two players take turns choosing columns, and the first player to align four of their markers either horizontally, vertically, or diagonally wins the game!

## Project Structure
The project is organized as a single Python script that contains the core logic for the Connect 4 game. The game can be played in two modes:
1. **Two Players**: Human vs. Human
2. **Single Player**: Human vs. AI

## Features
- Two-player mode with player markers (X or O).
- Automated win detection for horizontal, vertical, and diagonal lines.
- User-friendly prompts and input validation.
- Option to replay the game after a win.
### Without AI
- **Two Player Mode**: Two players can compete against each other by taking turns to drop their markers ('X' or 'O').
- **User Input**: Players can choose their markers and select columns to drop their discs.
- **Winning Conditions**: The game checks for wins after each turn, evaluating horizontal, vertical, and diagonal connections.
- **Board Display**: The current state of the board is displayed after every move.

### With AI
- **Single Player Mode**: A player can choose to play against a basic AI.
- **AI Logic**: The AI:
  - Tries to win if it has an immediate winning move.
  - Blocks the opponent's winning moves.
  - Chooses a random column if no immediate threats or wins are detected.

    
## How to Play
1. The game starts by asking Player 1 to choose their marker: `X` or `O`. Player 2 automatically gets the other marker.
2. Players take turns selecting a column (from 0 to 6) where they want to drop their marker.
3. The game checks if there are 4 markers in a row either horizontally, vertically, or diagonally. The first player to achieve this wins the game!
4. After a win, players are asked if they want to play again.

## Getting Started

### Prerequisites
Make sure you have Python installed on your system. You can download it from [Python's official site](https://www.python.org/downloads/).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Connect4Game.git
   ```
2. Navigate to the directory:
   ```bash
   cd Connect4Game
   ```
3. Run the game:
   ```bash
   python connect4.py
   ```

## Code Explanation

### Main Components:
- **`Connect4` class**: 
   - Initializes the game board and manages the game's logic.
   - Contains methods for displaying the board, checking if a column is full, playing a move, and detecting the win condition.

- **`play_game()` function**:
   - Manages the flow of the game, including player turns and input validation.
   - After each move, checks if a player has won the game.
   - Provides an option to replay the game after a win.

### Win Detection:
- **checkLines()**: Checks for four consecutive markers in rows or columns.
- **checkDiags()**: Detects diagonal wins both from top-left to bottom-right and from bottom-left to top-right.

## Example Game Flow
1. The board is displayed as a grid of 6 rows and 7 columns.
2. Players are asked to choose a column for their marker.
3. After every move, the board updates to reflect the latest changes.
4. The game checks for win conditions after each move.
5. When a player wins, the game displays the board and the winning player's name.

## Sample Output

```
Player 1, choose 'X' or 'O': X
You've chosen X. Player 2 will be O.
_ _ _ _ _ _ _
|   |   |   |   |   |   |   |
_ _ _ _ _ _ _
|   |   |   |   |   |   |   |
_ _ _ _ _ _ _
|   |   |   |   |   |   |   |
_ _ _ _ _ _ _
|   |   |   |   |   |   |   |
_ _ _ _ _ _ _
|   |   |   |   |   |   |   |
_ _ _ _ _ _ _
|   |   |   |   |   |   |   |
0    1    2    3    4    5    6
X's turn
Please select a column between 0 and 6: 
```
## Future Improvements
- **Enhanced AI**: Implementing more sophisticated AI algorithms (like minimax with alpha-beta pruning) for better gameplay.
- **Graphical User Interface (GUI)**: Adding a GUI using libraries such as Tkinter or Pygame for a more visually appealing experience.
- **Score Tracking**: Keeping track of wins and losses over multiple games.

## Conclusion
This Connect 4 project has evolved from an initial implementation without AI to an engaging single-player experience against an AI. The AI component was updated later to enhance gameplay, making it a foundational example of how to implement game logic and AI decision-making in Python.


## Author
- **Auhona Basu**

