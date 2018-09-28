_author_ = 'shail'

print("Please guess a number between 1 and 10 :")
guess = int(input())

if guess < 5:
    print("Please guess higher :")
    guess = int(input())
    if guess == 5:
        print("You guessed if correctly!")
    else:
        print("Sorry you have not guessed it correctly")

elif guess > 5:
    print("Please guess lower :")
    guess = int(input())
    if guess == 5:
        print("You guessed if correctly!")
    else:
        print("Sorry you have not guessed it correctly")
else:
    print("You got that correct the first time !!!")


