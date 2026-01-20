#number game 
import random
playing = True
number = str(random.randint(10,20))
print("i will generate a number from 10 to 20, and you have to guess the number one digit at a time")
print("the will be over when you guess correct number")

while playing:
    guess = input("give me your best guess:")
    if number == guess:
        print("you guessed the number correctly")
        break
    else:
        print("your guess is not correct. try again")