# 🗺️ U.S. States Game

A **US States guessing game** built with Python's `turtle` and `pandas`. Guess all 50 states on a blank map and track your progress!  

---

## 🚀 Features

- Interactive **map of the US** using Turtle graphics  
- Enter state names via a text prompt  
- Tracks correct guesses and progress  
- Save states you need to learn in `states_to_learn.csv`  

---

## 🧩 Tech Stack

- Python 3  
- `turtle` for graphics  
- `pandas` for data handling  

---

## 🛠️ Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/iremeroglu27/U.S.-States-Game.git
```
2. Install dependencies:
```bash
pip install pandas
```
3. Run the game:
```bash
python main.py
```

---

## 🎮 How to Play
- A blank US map will appear.
- A prompt will ask you to guess a state name.
- Correct guesses are written on the map.
- Type `Exit` to quit and save states you missed in `states_to_learn.csv`.
- Try to guess all 50 states!

---

## 🗂️ Files
- `main.py` → Main game script
- `50_states.csv` → Contains state names and coordinates for plotting
- `blank_states_img.gif` → Blank map of the US
- `states_to_learn.csv` → Stores the states you missed
- `.gitignore` → Ignores unnecessary files
  
---

## 📝 Notes
- Coordinates for each state are stored in `50_states.csv`.
- Correct guesses are displayed directly on the map using Turtle.
- The game is case-insensitive but capitalizes your input for display.

---

