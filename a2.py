import random
option=["rock","paper","scissors"]
user_choice=input("enter your choice(rock,paper,scissors):")
computer_choice=random.choice(option)
print(f"computer choice:{computer_choice}")
print(f"user choice:{user_choice}")
if user_choice==computer_choice:
    print("it's a tie")
elif user_choice=="rock"and computer_choice=="scissors":
    print("user win")
elif user_choice=="rock"and computer_choice=="rock":
    print("user win")
elif user_choice=="rock"and computer_choice=="paper":
    print("user win")
else:
    print("computer win")