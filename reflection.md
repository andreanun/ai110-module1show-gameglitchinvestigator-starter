# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

When we first ran the game, it looked playable on the surface once we started playing the game and guessing, the issues revealed themselves. The "New Game" button did nothing. Clicking it didn't actually reset the game because the status was never set back to "playing", so `st.stop()` kept blocking the rest of the app. The hints were also backwards: when our guess was too high, the game told us to go higher, and when we were too low it said go lower, which made it impossible to win by following the hints.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

We used Claude Code throughout the project. One correct suggestion was implementing the stub functions in `logic_utils.py`. Claude identified that all four functions raised `NotImplementedError` and that the implementations already existed in `app.py`, so it refactored them over. We verified this by running `pytest` and seeing all tests pass. One misleading moment was when we asked Claude to explain the `TypeError` branch inside `check_guess`, it initially described it as a reasonable safety fallback for non-integer inputs, which made us think it was fine. But that branch was actually the source of the "wins blocked on even attempts" bug, because the string comparison `g > secret` produced wrong results. We only caught it by actually playing the game and noticing we couldn't win on even-numbered attempts.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

We decided a bug was really fixed by testing it both with pytest and by manually playing the game. Passing tests alone weren't enough because some bugs only showed up through actual gameplay. The most useful test suite was `test_game_logic.py`: when we ran it before implementing `logic_utils.py`, every test failed with `NotImplementedError`, which clearly showed us the functions were stubs. After filling them in, all 8 tests passed, confirming the core logic was correct. Claude helped us understand what each test was checking, for example, it explained that `test_hard_difficulty_range_harder_than_normal` was verifying the upper bound of the range, which helped us connect that test directly to the Hard difficulty range bug.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because Streamlit reruns the entire Python script from top to bottom every time the user interacts with the page, so `random.randint()` was called fresh on every button click or keystroke, generating a new secret each time. Streamlit "reruns" means the whole script re-executes on every interaction, kind of like refreshing a webpage, except the app needs a way to remember things across those reruns. Session state (`st.session_state`) is like a small notebook that Streamlit keeps between reruns. Anything stored there survives the rerun. The fix was wrapping the secret generation in `if "secret" not in st.session_state`, so the random number is only picked once and then remembered for the rest of the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to carry forward is running tests before touching any code. Seeing all the `NotImplementedError` failures immediately told us exactly what needed to be done without having to read the whole codebase first. Next time I work with AI on a coding task, I'd verify AI explanations of existing code more skeptically, especially when the AI describes something as "intentional". In this project, code that looked like a safety feature turned out to be a bug. This project changed how I think about AI-generated code because I now treat it as a first draft that needs human review, not a finished product; the game looked functional on the surface but had seven bugs baked in that required careful investigation to find and fix.

<!-- Summary of all the bugs we fixed in app.py:

  1. New Game did nothing — status wasn't reset to "playing", so st.stop() blocked the game
  2. Input not cleared on New Game — added game_id to the input's key so Streamlit renders a fresh widget
  3. Hints were backwards — "Too High" said "Go HIGHER!" and "Too Low" said "Go LOWER!"
  4. Hard difficulty easier than Normal — range was 1–50 instead of 1–200; info text also hardcoded "1 to 100" regardless of difficulty
  5. Wins blocked on even attempts — secret was cast to a string on even attempts, so integer guesses could never match
  6. Score rewarded wrong guesses — "Too High" on even attempts added 5 points instead of deducting
  7. Attempts off by one — initialized to 1 instead of 0, so the first guess counted as attempt 2 -->
