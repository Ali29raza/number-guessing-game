import random
number= random.randrange(11)
no_guesses= 0
max_no_guesses=5

while max_no_guesses !=0:
    guess = input("make a guess: ")
    guess = int(guess)
    if guess== number:
        print("yippiii you made a correct guess")
        break
    else:
        no_guesses+=1
        max_no_guesses-=1
        print("your no. of incorrect guesses are: " ,no_guesses)
        print("remaining guesses: " , max_no_guesses)
else:
    print("Game over")
    print("your number of guesses are exhausted :(")
    print("the correct number is: " , number)
