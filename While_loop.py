# While loop example -> program to print the table
# program -> sum of all digits of a given number
# program -> keep accepting numbers from users till he/she enters a 0 and then find the avg


#1)

# num = int(input('ENTER the number: '))
#
# i = 1
# while i<11:
#     print(num,'*',i,'=',num*i)
#     i += 1

# Guessing Game
# generate a random integer between 1 and 100
import random
jackpot = random.randint(1,100)

guess = int(input('guess the number: '))
counter = 1

while guess != jackpot:
    if guess > jackpot:
        print("you've guessed number greater than jackpot!")
    else:
        print('guessed lower than jackpot')
    guess = int(input('guess the number: '))
    counter +=1
else:
    print('correct guess!')
    print('attempts you took ',counter)