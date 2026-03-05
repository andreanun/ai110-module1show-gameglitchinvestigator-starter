# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude Code
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

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

<!-- Here's a summary of all the bugs we fixed in app.py:

  1. New Game did nothing — status wasn't reset to "playing", so st.stop() blocked the game
  2. Input not cleared on New Game — added game_id to the input's key so Streamlit renders a fresh widget
  3. Hints were backwards — "Too High" said "Go HIGHER!" and "Too Low" said "Go LOWER!"
  4. Hard difficulty easier than Normal — range was 1–50 instead of 1–200; info text also hardcoded "1 to 100" regardless of difficulty
  5. Wins blocked on even attempts — secret was cast to a string on even attempts, so integer guesses could never match
  6. Score rewarded wrong guesses — "Too High" on even attempts added 5 points instead of deducting
  7. Attempts off by one — initialized to 1 instead of 0, so the first guess counted as attempt 2 -->
