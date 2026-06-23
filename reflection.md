# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- **What did the game look like the first time you ran it?**
  This is a number guessing game. I can choose the difficulty and then guess the number. The difficulty controls how many guesses I'm allowed, and every time I make a guess, a hint pops up telling me to go higher or lower.

- **Concrete bugs I noticed at the start:**
  1. **The hints were backwards.** I'm on easy mode and the secret number is 75. I typed 50 and it told me to go lower, but it should have told me to go higher.
  2. **The guessing page shows the wrong number range.** On easy mode, the left-hand sidebar says the range is 1 to 20, but the guessing page says "guess a number between 1 and 100."
  3. **The hard mode logic is wrong.** Its range is 1 to 50, but compared to normal difficulty (1 to 100), this shrinks the range and makes hard mode *easier* to guess.
  4. **The developer debug info panel doesn't update on "New Game."** After clicking New Game, it still showed the previous score and history, which should reset for the new game.
  5. **New attempts accumulate onto the old game.** Even after clicking New Game, new attempts are added to the previous score and history instead of starting fresh.
  6. **Switching difficulty keeps the old state.** When I switch from hard to normal difficulty, the score and history still use the previous values.
  7. **Easy mode secret number is out of range.** Easy mode's range is 1 to 20, but the secret number was 27, which is out of range.
  8. **Hard mode secret number is out of range.** Hard mode's range is 1 to 50, but the secret number was 92, which is out of range.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 12 (secret number is higher) | "Go higher" hint | "Go lower" hint | none |
| Guess of 30 in easy mode (range 1–20) | "Out of range — easy mode is 1 to 20" | Accepted the guess and hinted "go higher" | none |
| Guess of 92 (the correct number) in hard mode | Score in developer info shows 50 | Score in developer info shows -30; it didn't update | none |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
