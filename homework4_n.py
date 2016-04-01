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


def main():
    difficulty = input("Enter game mode: [E]asy [N]ormal [H]ard : ")
    game_list = total_word_list(difficulty.lower())
    winning_word = money_word(game_list)
    game_board = draw_board(winning_word)
    print(winning_word)
    print("\n" + game_board + "\n")

if __name__ == "__main__":
    main()
