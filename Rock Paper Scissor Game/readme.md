# 🎮 Rock Paper Scissors — Python

A simple **Rock Paper Scissors** game built with Python.
The player competes against the computer for **3 rounds**, with the score tracked throughout the game.

## ✨ Features

* 🎯 3-round game
* 🪨 Rock, 📄 Paper, ✂️ Scissor choices
* 🤖 Computer makes a random choice
* 🏆 Automatic score calculation
* ⚔️ Round-by-round results
* 🏅 Final tournament result
* ⚠️ Handles invalid number input
* ⏳ Includes a short delay while the computer chooses

## 🛠️ Technologies Used

* **Python**
* `random` module
* `time` module

## 🎮 How to Play

When the game starts, select one of the available options:

```text
1. Rock
2. Paper
3. Scissor
```

Enter the corresponding number.

The computer will randomly select its choice, and the winner of the round will be determined.

### 🏆 Winning Rules

| Player Choice | Beats      |
| ------------- | ---------- |
| 🪨 Rock       | ✂️ Scissor |
| 📄 Paper      | 🪨 Rock    |
| ✂️ Scissor    | 📄 Paper   |

If both choices are the same, the round is a draw.

## 📊 Scoring

* **Player wins** → Player gets `1` point
* **Computer wins** → Computer gets `1` point
* **Draw** → No points are added

After 3 rounds, the final scores are displayed and the tournament winner is announced.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Run the Python program

```bash
python rockpaperscisor.py
```

> Make sure Python is installed on your computer.

## 📁 Project Structure

```text
Rock-Paper-Scissors/
│
├── rockpaperscisor.py
└── README.md
```

## 🖥️ Example Output

```text
================= Welcome To The Game =================

==================================================
                    ROUND 1
==================================================

Select An Action
-----------------
1. Rock
2. Paper
3. Scissor
-----------------
Enter Your Choice : 1

----------------------------------------
You Choosed     : Rock
Computer Is Choosing...........

Computer Choosed : Scissor

----------------------------------------
              Rock  Vs  Scissor
----------------------------------------

----------------------------------------
                You Won
----------------------------------------

==================================================
                   FINAL SCORE
==================================================

Your Score       : 2
Computer's Score : 1

--------------------------------------------------
🏆 Congratulations! You won
--------------------------------------------------
```

## 📚 Concepts Practiced

This project helped practice:

* Variables
* Functions
* Conditional statements
* `if`, `elif`, and `else`
* `for` loops
* Exception handling with `try-except`
* User input
* Random number generation
* Global variables
* String formatting
* `time.sleep()`
* Basic game logic

## 👨‍💻 Author

**Hardik**

A beginner Python project created to practice programming fundamentals and game logic.
