import re

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

words = total_word_list('h')
print(words)
