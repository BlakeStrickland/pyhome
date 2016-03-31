import random

def is_integer(integer):
    try:
        user_guess = int(integer)
        return True
    except TypeError:
        print("Thats not a number!")
        return False
    except ValueError:
        print("Thats not a number!")
        return False

def too_low(user_input):
    return int(user_guess) < 0

magic_number =  random.randint(1,101)
count = 1
numbers_guessed = []
print("Let's play a game, Ill give you 5 trys to guess my number!")
while True:
    user_guess = input("Enter your guess >  ")
    if is_integer(user_guess):
        user_guess = int(user_guess)

        if user_guess == "":
            continue

        if count == 5:
            print("You were looking for {}".format(magic_number))
            break

        if magic_number == user_guess:
            print("You got it!")
            print("The magic number was {}".format(magic_number))
            break

        elif too_low(user_guess):
            print("Follow the rules!")

        elif user_guess > 100:
            print("Follow the rules!")
            continue


        elif user_guess in numbers_guessed:
            print("You already guessed that!")
            continue

        elif magic_number > user_guess:
            print("Your guess is too low!")
            numbers_guessed.append(user_guess)
            count += 1
            continue

        elif magic_number < user_guess:
            print("Your guess is too high!")
            numbers_guessed.append(user_guess)
            count += 1
            continue
