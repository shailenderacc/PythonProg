_author_ = 'shail'

print("Please guess a number between 1 and 10 :")

guess = int(input())

if guess != 5:
    if guess < 5:
            print("Please guess higher")
    else:
            print("Please guess lower")

    guess = int(input())

    if guess == 5:
            print("You guessed it correct")
    else:
            print("You guessed it wrong")
else:
    print("You guessed it the first time!!")


