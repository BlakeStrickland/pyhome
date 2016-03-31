import re

def is_palindrome(sentence):
    stripped = re.sub(r'[^A-Za-z]', "", sentence)
    stripped = stripped.lower()

    if stripped == reverse_string(stripped):
        return True
    else:
        return False

def reverse_string(text):
    if len(text) == 0:
         return ''
    print("text[0] = {}, \ntext[1:] = {}\n".format(text[0], text[1:]))
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
