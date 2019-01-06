# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

# 1)make a variable as the secret number - need the random module.
# 2) User input. need to loop back to this after program evaluates the input number with the generated number.
# 3) make the number of guesses another variable. need to update after every input from the user.
# 4) Print whether the guessed number was > or < the secret number. If <, print(too small), if >print (too large)
# 5) Print the number of tries needed to guess the number. Only count number of tries if the input number is different. 

import random

MAXLIMIT = 2000
secret = random.randint(1,MAXLIMIT)
tries = 0
oldguess = MAXLIMIT + 1
# alternative to below format. question = 'Try to guess the secret number from 1 to ' + str(MAXLIMIT) + ': '

try:
    while oldguess != secret:
        #guess=int(input(question))
        guess=int(input("Try to guess the secret number from 1 to {} : ".format(MAXLIMIT)))
        if guess> MAXLIMIT:
            quit()
        if oldguess != guess:
            tries=tries +1
        oldguess = guess
        if guess < secret:
            print("Too small")
        elif guess > secret:
            print("Too big")
        else:
            break
    print("You guessed it! It took you",tries,"tries.")
except:
    print("Failed")

