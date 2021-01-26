import random
from words import words
import string

def compu_num(words):
    pc_select = random.choice(words)
    while '-' in pc_select or ' ' in pc_select:
        pc_select = random.choice(words)
    
    return pc_select.upper()

def play():
    word = compu_num(words)
    print(word)
    word_letters = set(word)
    print(word_letters)
    alphabet = set(string.ascii_uppercase)
    print(alphabet)
    used_letters = set()

    contador = 6

    while len(word_letters) > 0 and contador > 0:
        print(f'you have {contador}, lives left and you have used these letters: {" ".join(used_letters)}')
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f'Current word: {" ".join(word_list)}')


        user_letter = input('Please type a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                contador -= 1
                print(f'Your letter {used_letters} is not in the word.')

        elif user_letter in used_letters:
            print(f'You already insered {user_letter}')

        else:
            print(f'That is not a valid letter')
    
    if contador == 0:
        print('さよなら')
    else:
        print('Gnaste')

if __name__== '__main__':
    play()