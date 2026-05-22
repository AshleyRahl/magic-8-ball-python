"""
Magic 8 Ball:

This project simulates a Magic 8 Ball toy in the command-line interface.
It accepts yes-or-no questions from the user and provides a random response from a predefined list of answers.
The list of responses includes affirmative, neutral, and negative answers - from the classic 20 Magic 8 Ball toy answers.
The user can ask multiple questions until they choose to exit the program by typing "quit" or "q".

Implementation Details:
- The program uses the `random` module to select a random response from the list of possible answers.
- The `time` module is used to add delays, simulating the shaking and thinking process of the Magic 8 Ball, enhancing the user experience.
- The program runs in a loop, allowing the user to ask multiple questions until they decide to exit.

Features:
- A welcoming message that explains how to use the Magic 8 Ball.
- A list of 20 classic Magic 8 Ball responses.
- The ability for the user to exit ("quit" or "q").

"""

import random # Import the random module to generate random numbers
import time # Import the time module to add delays for a better user experience

# List of possible responses for the Magic 8 Ball
# responses = ["YES", "NO", "MAYBE"]
responses = [
    # Affirmative Answers (Yes)
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes - definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    # Neutral Answers (Maybe / Try Again)
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    # Negative Answers (No)
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

# Welcome message
print("--- Welcome to the Magic 8 Ball! ---")
print("Ask any yes-or-no question and receive your answer.")
print("To exit, type 'quit' or 'q'.\n")

# Loop to allow the user to ask multiple questions
while True:
    # Prompt the user to ask a yes-or-no question
    user_question = input("Ask your question: ")

    # if the user types "quit" or "q", exit the program
    if user_question.lower() == "quit" or user_question.lower() == "q":
        print("Thanks for playing! Goodbye...")
        break # This stops the loop

    print("\nShaking the Magic 8 Ball...") # Simulate shaking the Magic 8 Ball
    time.sleep(1) # Add a delay for a better user experience

    print("Thinking...\n") # Simulate the Magic 8 Ball thinking
    time.sleep(1.5) # Add a delay for a better user experience

    # Pick a random response from the list of responses
    magic_ball_answer = random.choice(responses)

    # Display the Magic 8 Ball's answer
    print("The Magic 8 Ball says: ", magic_ball_answer)
    print()