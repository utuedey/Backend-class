import random
random = random.randint(1,100)
guess = None

def guess_game():
    print("Welcome to GUESS GAME!!! This would be fun." +
          "\nIn this game, you'd guess a number within a given range.")
    print("\n")
    count = 1
    trial = 5
    if random % 2 == 0:
        print("The number is an even number")
    else:
        print("The number is an odd number")
    while count <= 6:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        
            if guess < random:
                print("Too low.. You have " + str(trial) + " trial(s) left")
            elif guess > random:
                print("Too high... You have " + str(trial) + " trial(s) left")
            else:
                print("Congratulations, You have guessed correctly!!!")
                break
        except ValueError:
            print("You have entered an invalid response, enter a number between 1 and 100")
        count += 1
        trial -= 1
        if count >6:
            print("You Lose. The number was " + str(random))

def replay():
    while True:
        play_again = input("Would you like to play again?  'yes/no' ").title()
        while play_again not in ["Yes", "No"]:
            play_again = input("Invalid input! You must choose between 'yes' and 'no'" +
                               " Would you like to play again? 'yes/no' ").title()
        if play_again != "Yes":
            print("Thanks for playing...")
            break
        else:
            guess_game()


guess_game()
replay()
            
        



