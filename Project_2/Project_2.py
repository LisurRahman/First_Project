# Rock,Scissors,Paper Game
import random
user = None
options = ("rock", "scissors", "paper")
computer = random.choice(options)
user = input("Enter your choice from [rock/scissors/paper]:")

print(f"Your choice is: |{user}|")
print(f"My choice is: |{computer}|")

if computer == user:
    print("    \n   congratulation! You win the game.")
else:
    print("  \n  Oops!!! You loss the game.      \n     Try again!!")










































