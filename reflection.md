# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The first bug that I noticed was that the hints were backwards like instead of telling me to guess higher, it kept on telling me to guess lower. Another bug is that even though I click the "New Game" button, it doesnt work.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|56 | go higher |  go lower | Instead of telling me to go higher, it told me to guess lower. |

|Clicked on "New Game" button | Start a new game | It gave me new attempts, but while I click submit guess, it's not going forward, and the game is not restarting  | It's not restarting the game, and not going forward. |

| 56, 40, 37, 30, 24, 21, 18,| "Go Lower"/ "Go Higher"| "Out of Attempts! The Secret was 94."|Even though I still have one attempt left, its ending the game one attempt early. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude AI tool for this project. One thing that it suggested was the change in the code for the inverted hint. It was a little incorrect which I verfified by myself, and asked it to change it correctly. One thing it suggested me wrong was to create a new file and copy the code for the refactory, which I did not do as it was misleading
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I decided whther my bug was really fixed by running it, and making sure that the test cases passed.
I did the pytest, and the test made sure that it told the user crrectly whether to guess lower or higher by chaning the numbers. It showed me that my code was correct. Yes, AI did help my design my test, as it helped me change it and cover more situations.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns is basically where everytime you change somthing, it reruns the whole Python Script. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think that I would like to use the prompting strategy, by being as specific as possible, to make sure that it is fixing the correct things. This project really improved my confidence of AI- generated code, as it was really accurate and helped me fix it where it was wrong.
