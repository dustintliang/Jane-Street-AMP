import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

def get_feedback(guess: str, secret_word: str) -> str:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word

        Returns:
            str: Feedback string, based on comparing guess with the secret word
    
        Examples
        >>> get_feedback("lever", "EATEN")
        "-e-E-"
            
        >>> get_feedback("LEVER", "LOWER")
                "L--ER"
            
        >>> get_feedback("MOMMY", "MADAM")
                "M-m--"
            
        >>> get_feedback("ARGUE", "MOTTO")
                "-----"
    '''
        ### BEGIN SOLUTION
    if len(guess) == len(secret_word):
        returned_str = ''
        pos = len(secret_word)-1
        guess1 = list(guess.upper())
        for letter in guess1[::-1]:
            if letter == secret_word[pos]:
                returned_str += letter
            if letter not in secret_word:
                returned_str += '-'
            if letter != secret_word[pos] and guess1.count(letter) <= secret_word.count(letter):
                returned_str += letter.lower()
            if letter != secret_word[pos] and guess1.count(letter) > secret_word.count(letter) and secret_word.count(letter) >= 1:
                guess1.pop(pos)
                returned_str += '-'
            pos -= 1

        final = ''
        for letter in returned_str[::-1]:
            final += letter
        return final           
    else:
        return('')
        ###END SOLUTION

def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
        
        Args:
         guesses (list): A list of string guesses, which could be empty
         feedback (list): A list of feedback strings, which could be empty
         secret_words (set): A set of potential secret words
         valid_guesses (set): A set of valid AI guesses
        
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    ### BEGIN SOLUTION
    stored_list = [0, 1, 2, 3, 4]
    lower_set = set()
    dictionary = dict()
    invalid_letters = set()
    if len(guesses) == 0:
        print('')
    else:
        pos = 0
        while pos < len(guesses):
            letter_pos = 0
            while letter_pos < len(guesses[pos]):
                if feedback[pos][letter_pos] == feedback[pos][letter_pos].upper() and feedback[pos][letter_pos].isalpha():
                    stored_list[letter_pos] = feedback[pos][letter_pos]
                if feedback[pos][letter_pos] == feedback[pos][letter_pos].lower() and feedback[pos][letter_pos].isalpha():
                    lower_set.add(feedback[pos][letter_pos])
                if feedback[pos][letter_pos] == '-' and (feedback[pos].count(guesses[pos][letter_pos].upper()) + feedback[pos].count(guesses[pos][letter_pos].lower())) >= 1:
                    dictionary[guesses[pos][letter_pos].upper()] = (feedback[pos].count(guesses[pos][letter_pos].upper()) + feedback[pos].count(guesses[pos][letter_pos].lower()))
                if feedback[pos][letter_pos] == '-' and (feedback[pos].count(guesses[pos][letter_pos].upper()) + feedback[pos].count(guesses[pos][letter_pos].lower())) == 0:
                    invalid_letters.add(guesses[pos][letter_pos])
                letter_pos += 1
            pos += 1
    secret_words = get_secret_words()
    for word in secret_words:
        valid_word = True
        for letter in word:
            position = 0
            for valid in stored_list:
                if type(valid) == str:
                    if word[position] != stored_list[position]:
                        valid_word = False
                        break
                position += 1
            if letter in invalid_letters:
                valid_word = False
        for i in lower_set:
            i = str(i).upper()
            if i not in word:
                valid_word = False
        for l, c in dictionary.items():
            if word.count(str(l).upper()) > c:
                valid_word = False
                break
        if valid_word == True:
            return word
    ### END SOLUTION 

# TODO: Define and implement your own functions!

#bug where it keeps adding on to incorrect guesses and loop never ends even without the while True statement
def get_guess():
    while True:
        guess_input = input('Guess a 5 letter valid word: ' )
        upper_guess = guess_input.upper()
        if upper_guess in get_valid_wordle_guesses():
            return guess_input
        else:
            guess_input = ''
            print('Not in word list. Try again.')

'''def get_hint(returned_str: str, secret_word: str):
    for letter in returned_str:
        if letter.upper() == letter:
            continue
        if letter.lower() == letter:
            letter1 = letter.upper()
            test = False
            while test == False:
                position = secret_word.find(letter1)
                if letter1 == secret_word[position]:
                    secret_word.replace(letter1, '1')
                else:
                    return letter, 'is in the', position+1, 'position'
        else:
            position = secret_word.find(letter1)
            return letter'''


'''def play_game(time_limit: int, letters: list, explorer:AnagramExplorer) -> list:

    secret_word = random.choice(get_secret_words())

    guesses = [] 
    quit = False

    start = time.perf_counter() #start the stopwatch (sec)
    stop = start + time_limit

    while time.perf_counter() < stop and not quit:
        guess = input('')
        if guess.strip() == "quit":
            quit = True
        elif guess.strip() == "hint":
            print(f"Try working with: {explorer.get_most_anagrams(letters)}")
        else:
          tuple_guess = parse_guess(guess)
          if len(tuple_guess[0]) > 1:
            guesses.append(tuple_guess)
          else:
            print("Invalid input")

        print(f"{letters} {round(stop - time.perf_counter(), 2)} seconds left")

    return guesses'''
        
#Fore.COLOR not working
def wordle_colors(guess: str, returned_string: str):
    color_string = ''
    pos = 0
    for letter in returned_string:
        if letter.upper() == letter and letter != '-':
            color_string += Back.GREEN + Fore.WHITE + str(letter)
        if letter.lower() == letter and letter != '-':
            color_string += Back.YELLOW + Fore.WHITE + str(letter)
        if letter == '-':
            color_string += Back.BLACK + Fore.WHITE + guess[pos]
        pos += 1
    return color_string     

'''def counter_to_create_mult_blocks(colorful: str, guess_count: int) -> str:'''


def start_game():
    secret_word1 = get_secret_words()
    secret_word = random.choice(list(secret_word1))
    name = str(input('What is your name?\n'))
    print('\nWelcome to wordle', name,'!\n')
    print('You will get 5 chances to guess a 5 letter secret word.\n')
    print('If a letter in your guessed word is in the secret word and in the right spot, it will be green.\n')
    print('If a letter in your guessed word is in the secret word and in the wrong spot, it will be yellow.\n')
    print('If a letter in your guessed word is not in the secret word or its count is higher than the count in the secret word, it will be black.\n')
    while True:
        user_response = str(input('If you understand, type "yes".\n'))
        if user_response == 'yes':
            return secret_word, name
        else:
            print('Just type yes', name, '.')

if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    guess_count = 0
    stored_colorful = ''
    guess_list = []
    secret_word, name = start_game()
    while guess_count < 5:
        guess = get_guess()
        returned_string = get_feedback(guess, secret_word)
        colorful = wordle_colors(guess, returned_string)
        guess_count += 1
        if guess_count == 1:
            print(colorful)
            stored_colorful += "\n"+colorful 
        else:
            stored_colorful += "\n"+colorful
            print(stored_colorful)
        if guess.upper() == secret_word:
            print('Congrats! You won in', guess_count, 'turns!')
            quit()
    print(f'You failed! Never play wordle again {name} you unskilled person!')

    
    #inputs, 5 guesses, print feedback