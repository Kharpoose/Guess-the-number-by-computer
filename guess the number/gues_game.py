import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number betwen 1 and {x}: "))
        if guess > random_number:
            print('Sorry, you guessed too high')
        elif guess < random_number:
            print('Sorry, you guessed too low')    

    print(f'Yeyy you nail it!! {x} is correct number.')        
        

guess(10)
