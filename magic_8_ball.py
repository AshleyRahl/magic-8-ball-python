"""
Magic 8 Ball:
A Magic 8 Ball is a toy used for fortune-telling or seeking advice. 
It provides random answers to yes-or-no questions. 
This program simulates the Magic 8 Ball by generating random responses to user questions.
"""

import random # Import the random module to generate random numbers

# List of possible responses for the Magic 8 Ball
# responses = ["YES", "NO", "MAYBE"]
responses = [
    # Affirmative Answers (Yes)
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    # Neutral Answers (Maybe / Try Again)
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    # Negative Answers (No)
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Welcome message
print("--- Welcome to the Magic 8 Ball! ---")

# Prompt the user to ask a question
user_question = input("Ask your question: ")

print("Thinking...\n") # Simulate the Magic 8 Ball thinking

# Pick a random response from the list of responses
magic_ball_answer = random.choice(responses)

# Display the Magic 8 Ball's answer
print("The Magic 8 Ball says: ", magic_ball_answer)
# print(magic_ball_answer)