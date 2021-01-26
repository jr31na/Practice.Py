import random
from words import words
import string

# ❶
def get_valid_word(words):
    pc_select = random.choice(words)  # randomly chooses something from the list
    while '-' in pc_select or ' ' in pc_select: #While - or space is in the word, keep chosen the same word 
        pc_select = random.choice(words) 
    print(f'Hola yo el pc seleccione {pc_select}')
    return pc_select.upper() #When stop iterated im going to get a word that dont have space or -


def hangman():
    # ❷
    word = get_valid_word(words) # Pc select a valid word and I save in it in variable word
    print(F'Hola escoji esta letra para que la adivinaras {word}')
    word_letters = set(word)  # Create a diccionary with the letters that are in word
    print(F'Hola la palabra que seleccione contiene las siguinetes letras {word_letters}')
    alphabet = set(string.ascii_uppercase) #import uppercase leters in the english diccionary 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(F'Hola soy las letras del abecedario desordenadas {alphabet}')
    used_letters = set()  # save letters that the user has guessed
    print(F'Hola yo guardo las palabras en {used_letters}')

    # ➓
    lives = 6

    # Getting user input / be able to keep guessing until user guess the word
    # ❻
    while len(word_letters) > 0 and lives > 0: #while the len of word_letters is more than 0 and I have more than one live keep iterating 
        # letters used to show user what they have been using
        # " ".join(['a', 'b', 'cd']) --> 'a b cd' {turn the list in a sting}
        # ❽
        print(f'You have, {lives}, lives left and you have used these letters: {" ".join(used_letters)} ') #used_letters will be in a sting sepatate with a space # Show the user what current word is with spaces (ie W - - - -  R D)
        # ❾
        word_list = [letter if letter in used_letters else '-' for letter in word] #Create a list where ever single insert letter is shown if it is in used_letters. else → all the word that user havent guess keep it with -----
        print('Current word: ', ' '.join(word_list)) #join with a space to create a string

        # ❸
        user_letter = input('Guess a letter: ').upper() #Ask the user for a letter and save it in upper case
        if user_letter in alphabet - used_letters: #if this is a valid letter in the alphabet that I haven't use yet
            used_letters.add(user_letter) # add (user_letter) to my used_letter
            if user_letter in word_letters: # if the user_letter is in the word_letter
                word_letters.remove(user_letter) #I am going to remove the user_letter form word_letter 
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
        # ❹
        elif user_letter in used_letters: #if the user_letter is in used_letters
            print('\nYou have already used that letter. Guess another letter.') #print.....
        # ❺
        else: #Otherwise [when user type a symbol or something that is not a letter]
            print('\nThat is not a valid letter.') #print an error message 

    # ❼
    # gets here when len(word_letters) == 0 OR when lives == 0
    # ❶❶
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()