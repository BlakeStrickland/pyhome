import re

def stripped(sentence):
    return re.sub(r'[^A-Za-z]', "", sentence).lower()

def is_palindrome(sentence):
    if stripped(sentence) == reverse_string(sentence):
        return True
    else:
        return False


def back_to_front(text):
    clean_text = stripped(text)
    if len(clean_text) == 0 or len(clean_text) == 1:
        return False
    elif len(clean_text) < 4:
        if clean_text[0] == clean_text[-1]:
            return True
        else:
            return False
    else:
        if clean_text[0] == clean_text[-1]:
            return back_to_front(clean_text[1:-1])
        return False

def reverse_string(text):
    if len(text) == 0:
         return ''
    print("text[0] = {}, \ntext[1:] = {}\n".format(text[0], text[1:]))
    text = stripped(text)
    return reverse_string(text[1:]) + text[0]

def main():
    possible_palin = input("Test your palindrome: ")
    if is_palindrome(possible_palin):
        print("Thats a dope one, gonna have to remember it.")
        return True
    else:
        print("Not a palindrome")
        return False

if __name__ == '__main__':
    main()
