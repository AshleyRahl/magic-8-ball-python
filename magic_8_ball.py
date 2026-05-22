"""
Magic 8 Ball:
A Magic 8 Ball is a toy used for fortune-telling or seeking advice. 
It provides random answers to yes-or-no questions. 
This program simulates the Magic 8 Ball by generating random responses to user questions.
"""

import random # Import the random module to generate random numbers

# List of possible responses for the Magic 8 Ball
responses = ["YES", "NO", "MAYBE"]

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