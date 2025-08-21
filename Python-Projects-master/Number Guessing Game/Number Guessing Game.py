import random

def easyfun():
    global att
    print(f"you have {att} attempts remaining to guess the number!")
    guess=int(input("Make a guess:"))
    if guess==think_value:
        print(f"you have guessed correct and the value is {guess}")
    else:
        if guess<think_value:
            print("your guess is too low.")
            print("guess again.")
            att=att-1
            if att==0:
                print("you have lossed the game.")
                exit()
            else:
                easyfun()
        else:
            print("your guess is too high.")
            print("guess again.")
            att = att - 1
            if att == 0:
                print("you have lossed the game.")
                exit()
            else:
                easyfun()
def hardfun():
    global att
    print(f"you have {att} attempts remaining to guess the number!")
    guess = int(input("Make a guess:"))
    if guess == think_value:
        print(f"you have guessed correct and the value is {guess}")
    else:
        if guess < think_value:
            print("your guess is too low.")
            print("guess again.")
            att = att - 1
            if att == 0:
                print("you have lossed the game.")
                exit()
            else:
                easyfun()
        else:
            print("your guess is too high.")
            print("guess again.")
            att = att - 1
            if att == 0:
                print("you have lossed the game.")
                exit()
            else:
                easyfun()


print("let me think a number between 1 and 50!")
think_value=random.randint(1,50)
#print(think_value)
level=input("choose level of difficulty...Type 'easy' or 'hard':").lower()
if level=="easy":
    att=10
    easyfun()
elif level=='hard':
    att=5
    hardfun()
