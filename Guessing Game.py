'''=============================================================
= Program Author - Kevin E. De Leon                            =
= Date Written - 17 October 2021                               =
= Purpose - Create a simple guessing game using random nubmers =
============================================================='''

print(" - It's D.I.A again! Here to play a game with you.")
print(" - It's simple, guess the right number and you win!")
print(" - Guess wrong too many times and- lets not get to that :)")




import random
 
random_number = random.randint(1,100)
tries = 0
 
username = input("First, What's your Username?: ")
 
print("Hello", username+",", )
 
question = input("Would you Like To Play A Game ? [Y/N] ")
 
if question == "n":
    print("oh..okay")
 
if question == "y":
    print("I'm Thinking Of A Number Between 1 & 100")
    guess = int(input("Have a Guess :"))
    if guess > random_number:
        print("Guess Lower...")
    if guess < random_number:
        print("Guess Higher...")
 
    while guess != random_number:
        tries += 10
        guess = int(input("Try Again : "))
        if guess <random_number:
            print("Guess Higher...")
        if guess >random_number:
            print("Guess Lower...")

            
    if guess == random_number:
        print("You're Right! You win! The Number Was", random_number, "and it only", tries, "tries!")
 
