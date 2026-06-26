import random
play_again = "y"
while (play_again == "y"):
    random_number = random.randint(1,10)
    life_counter = 5
    print(f'You have {life_counter} lives ')
    guessed_number = int(input("Enter a random value from 1-10 "))
    count = 1
    if (guessed_number == random_number):
         print(f'Your guess was correct and you guessed it in {count} number of gusses without any lives lost')
         play_again = input("Do you want to play again (y/n): ").lower()
    else:
        while(guessed_number != random_number and life_counter !=0):
            life_counter = life_counter-1
            count = count + 1
            guessed_number = int(input("Enter a random value from 1-10 "))
            print(f'You lost a life, you have {life_counter} lives left')
    if(life_counter != 0):
        print(f'Your guess was correct and you guessed in {count} number of guesses with {life_counter} lives left ')
    else:
        print(f'No lives left you lost')
    play_again = input("Do you want to play again (y/n) ").lower()
    









