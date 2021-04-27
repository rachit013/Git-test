import random

highest = 1000
answer = random.randint(1, highest)

# print(answer)
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
        # guess = int(input())
        # if guess == answer:
        #     print("well done you guessed it")
        # else:
        #     print("sorry you didn't guess correctly")

# while guess != answer:
#     if guess < answer:
#         print("guess higher")
#     else:
#         print("guess lower")
#     guess = int(input("please guess a number between 1 to 10: "))
#
# if guess == answer:
#     print("Congratulation you guessed it")
    
    

        
    
    
