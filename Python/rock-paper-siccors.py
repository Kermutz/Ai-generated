# Kermutz comment here
# Its generated by ai and is a bit dumb its 1,2,3 to choose which one
# You want

import random

print("Rock, Paper, Scissors")

# set the computer's choice

computer = random.randint(1, 3)

# set the player's choice

player = int(input("Enter your choice: "))

# display the computer's choice

if computer == 1:
    print("The computer chose Rock.")
elif computer == 2:
    print("The computer chose Paper.")
else:
    print("The computer chose Scissors.")

# display the player's choice

if player == 1:
    print("You chose Rock.")
elif player == 2:
    print("You chose Paper.")
else:
    print("You chose Scissors.")

# display the winner

if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
else:
    print("You lose!")
