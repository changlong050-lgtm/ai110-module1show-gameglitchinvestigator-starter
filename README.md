# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Describe the game's purpose
This is a number-guessing game built with Streamlit. The player selects a difficulty level (Easy, Normal, or Hard), which sets both the number range and the number of allowed guesses. The player then guesses the secret number, and after each guess the game gives a hint telling them to go higher or lower, until they either guess correctly or run out of attempts.

### Detail which bugs you found
1. **Hints were backwards** — when the guess was too low, the game said "go lower" instead of "go higher" (the high/low logic was reversed).
2. **Secret number out of range** — in Easy mode the range was 1–20, but the secret number could be generated outside that range (e.g. 27).
3. **Inconsistent range display** — the sidebar showed the range as 1–20 while the guessing page said "guess a number between 1 and 100."
4. **State not resetting on New Game** — clicking "New Game" did not reset the score and history; new attempts accumulated onto the previous game.

### Explain what fixes you applied
- Fixed the reversed high/low hint logic so the correct direction is returned (when `guess > secret`, the game now says "go lower," and vice versa).
- Fixed the secret-number generation so it always falls within the selected difficulty's range.
- Refactored the core logic (such as `check_guess`) out of `app.py` and into `logic_utils.py`, then updated the imports in `app.py`.
- Added a `pytest` test in `tests/test_game_logic.py` to verify the hint logic, and confirmed all tests pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Easy mode (range 1–20)
2. User enters a guess of 5
3. Game returns "Too Low — go higher"   ← (the high/low hint bug is now fixed)
4. User enters a guess of 15 → "Too High — go lower"
5. User enters a guess of 12 → "Correct!"
6. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest
============================================================== test session starts ===============================================================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\at252\OneDrive\Documents\ai110\project1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 6 items

tests\test_game_logic.py ......                                                                                          [100%]

=============================================================== 6 passed in 0.05s ================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
