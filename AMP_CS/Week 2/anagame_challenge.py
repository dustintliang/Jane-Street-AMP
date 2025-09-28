from typing import Type
from AnagramExplorer import AnagramExplorer
from valid_anagame_words import get_valid_word_list

def get_highest_score(letters:list[str], explorer: Type[AnagramExplorer]):
    '''Determines the highest possible score from a given list of 7 letters 
       based on AnaGame scoring:
        - 3 letter anagram pair: 1pt      are, ear
        - 4 letter anagram pair: 2pt      balm, lamb
        - 5 letter anagram pair: 3pt      sneak, snake
        - 6 letter anagram pair: 4pt      actors, costar
        - 7 letter anagram pair: 5pt      allergy, gallery

       Args:
        letters (list[str]): A list of 7 letters form which all words must be formed
        explorer (AnagramExplorer): An AnagramExplorer helper object
        
       Returns:
        int: an integer score
    '''
    ### BEGIN SOLUTION

    ### END SOLUTION
    
def get_highest_scoring_letters(explorer: Type[AnagramExplorer]) -> list:
    '''Determines which 7 letters produce the highest score for a given word list
       based on AnaGame scoring:
        - 3 letter anagram pair: 1pt      are, ear
        - 4 letter anagram pair: 2pt      balm, lamb
        - 5 letter anagram pair: 3pt      sneak, snake
        - 6 letter anagram pair: 4pt      actors, costar
        - 7 letter anagram pair: 5pt      allergy, gallery

       Args:
        explorer (AnagramExplorer): An AnagramExplorer helper object
        
       Returns:
        list: a list of 7 letters    
    '''
    ### BEGIN SOLUTION
   
    ### END SOLUTION 

def get_most_word_pair_letters(explorer: Type[AnagramExplorer]) -> list:
    '''Determines which 7 letters produce the most anagram word pairs for
       a given word list.

       Args:
        explorer (AnagramExplorer): An AnagramExplorer helper object
        
       Returns:
        list: a list of 7 letters
    
    '''
    ### BEGIN SOLUTION
   
    ### END SOLUTION 

if __name__ == "__main__":
    my_explorer = AnagramExplorer(get_valid_word_list())
    letters = ["p", "o", "t", "s", "r", "i", "a"]

    score = get_highest_score(letters, my_explorer)
    print(score)

    best_letters1 = get_highest_scoring_letters(my_explorer)
    print(f"{best_letters1} has the potential to produce the highest score in AnaGame")
    
    best_letters2 = get_most_word_pair_letters(my_explorer)
    print(f"{best_letters2} has the potential to produce the most anagram word pairs in AnaGame")