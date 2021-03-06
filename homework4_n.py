import re
import random

all_words = []
def total_word_list(difficulty):
    with open('/usr/share/dict/web2', 'r') as word_file:
        for line in word_file:
            for word in line.split():
                word = re.sub('[^A-Za-z]', '', word).lower()
                if difficulty.lower() == 'e':
                    if 4 <= len(word) <= 6:
                        all_words.append(word)
                elif difficulty.lower() == 'n':
                    if 6 <= len(word) <= 8:
                        all_words.append(word)
                elif difficulty.lower() == 'h':
                    if len(word) >= 8:
                        all_words.append(word)
                else:
                    total_word_list(difficulty)
        return all_words

def money_word(my_list):
    return random.choice(my_list)

def draw_board(word):
    b = ("_ " * (len(word)))
    return b

def get_guess():
    user_guess = input("Please enter a letter: ")

def game_guess(guess, winning_word):
    if len(guess) >= 2:
        print("Your guess can only be 1 character")
        get_guess()
    elif len(guess) == 1:
        if guess in winning_word:
            winning_word.append(guess)



def main():
    difficulty = input("Enter game mode: [E]asy [N]ormal [H]ard : ")
    game_list = total_word_list(difficulty.lower())
    winning_word = money_word(game_list)
    game_board = draw_board(winning_word)
    print(winning_word)
    print("\n" + game_board + "\n")

    # while "_ " in game_board:
if __name__ == "__main__":
    main()
