import random

print("Welcome to the guessing number game!")
print("you choose a range(integer only) and guess the number, if it's out of range we will have a notification for you!")
continue_playing = True
while(continue_playing == True):
    while(True):
        try: 
            lower_bound = int(input("Enter your lower bound number: "))
        except ValueError:
            print("Lower bound is not a number, please give a different one!")
            continue
        try:
            upper_bound = int(input("Enter your upper bound number: "))
        except ValueError:
            print("Upper bound is not a number, please give a different one!")
            continue

        if(lower_bound >= upper_bound):
            print("lower bound should be smaller than upper bound!")
            continue
        break
    res = random.randrange(lower_bound, upper_bound)
    while(True):
        try:
            val = int(input("what's your lucky guess?: "))
        except ValueError:
            print("your input is not a number! please input again.")
            continue
        if(val < res):
            print("Try Again! You guessed too small")
        elif(val > res):
            print("Try Again! You guessed too high.")
        else:
            print("Congratulations!")
            break
    while(True):
        print("do you want to continue?(y/n) ")
        next_game = input().strip().lower()
        if(next_game == "n"):
            continue_playing = False
        elif(next_game !='y'):
            print("please give valid answer")
            continue
        break

