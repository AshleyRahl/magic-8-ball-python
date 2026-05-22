# Magic 8-Ball (Python Basic Edition)

A classic console-based Magic 8-Ball application built in Python to practice programming fundamentals. 

## Core Concepts Implemented:
 * **Lists:** To manage and organize the 20 treditional responses.
 * **User Input:** For prompting the user's question and exit command.
 * **Randomness:** Importing Python's `random` module, to pick answers from given list
 * **Control Flow:** A `while` loop for continuous playing and `if` statment for user interaction.
 * **Time Managment:** Importing the `time` module to add pacing (`time.sleep()`)

## 1. Completed Features:
* **Step 1 (Basics):** Welcome message and core user input/output execution.
* **Step 2 (Traditional Responses):** Expanded the basic choices to include all 20 traditional Magic 8-Ball answers.
* **Step 3 (Continuous Gameplay):** Added a loop so the user can ask multiple questions, with input normalization allowing a clean exit by typing `quit` or `q`.
* **Step 4 (Immersive UX):** Integrated a simulated "shaking" and "thinking" dramatic pause delay.

## 2. Logic Flow (Pseudo-code)
1. IMPORT the necessary randomness tool.
2. CREATE a collection of 8-ball answers.
3. PRINT a welcome message.
4. ASK the user for text input.
5. CHOOSE a random item from the collection.
6. PRINT the chosen item to the screen.

## How to Run the Project:
1. Ensure you have Python installed on your local machine.
2. Clone this repository to your desktop.
3. Open your terminal, navigate into the project folder, and run:
   
```bash
   python magic_8_ball.py
```