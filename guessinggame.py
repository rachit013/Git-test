import random

highest = 1000
answer = random.randint(1, highest)
guess = 0
print("please guess a number between 1 to {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Thank you, please come next time")
        break
    if guess == answer:
        print("well done you guessed it")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")

    
    
