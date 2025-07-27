# import random

# print("THIS IS THE GAME OF ROCK PAPER SCISSORS")

# options = ["rock", "paper", "scissors"]
# userchoice = input("ENTER YOUR CHOICE: ").lower()
# computerchoice = random.choice(options)

# if userchoice not in options:
#     print("INPUT CHOICE ISN'T VALID")
# else:
#     print(f"\nYOU CHOSE: {userchoice}")
#     print(f"COMPUTER CHOSE: {computerchoice}")

#     if userchoice == computerchoice:
#         print("MATCH TIE")
#     elif (
#         (userchoice == "rock" and computerchoice == "paper") or
#         (userchoice == "paper" and computerchoice == "scissors") or
#         (userchoice == "scissors" and computerchoice == "rock")
#     ):
#         print("COMPUTER WIN!")
#     else:
#         print("YOU WIN!")






import random
options=["rock","paper","scissors"]
user=input("USER INPUT :").lower()
python=random.choice(options)
print("PYTHON CHOICE :",python)
if user not in options:
    print("inavalid choice")
elif user==python:
    print("MATHCH TIE")
elif user=="rock":
    if python=="paper":
        print("PAPER COVER ROCK AND PYTHON WIN!")
    if python=="scissors":
        print("ROCK SMASHED THE SCISSORS AND YOU WIN!")
elif user=="paper":
    if python=="rock":
        print("PAPER COVER ROCK AND YOU WIN!")
    if python=="scissors":
        print("PAPER CUT BY SCISSORS AND PYTHON WIN!")
elif user=="scissors":
    if python=="paper":
        print("PAPER CUT BY SCISSORS AND YOU  WIN!")
    if python=="rock":
        print("ROCK SMASHED THE SCISSORE AND PYTHON WIN!")
else:
    print("SOMTHING WENT WRONG")

print("THANK FOR PLAYING")