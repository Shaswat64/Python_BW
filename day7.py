# guess a random number
# print(random.random())       #decimal value
# c = [1,2,3,4,5,6,7]
# print(random.choice(c))      #    #gives a random number from the set
import random
random_number = random.randint(1,10)
guessed_number = 1
count = 1
if (guessed_number == random_number):
    print(f'Your guess was correct and you guessed it in {count} number of gusses')


else:
    while(guessed_number != random_number):
        count = count + 1
        guessed_number = int(input("Enter a random value from 1-10 "))
    print(f'Your guess was correct and you guessed in {count} number of guesses ')





