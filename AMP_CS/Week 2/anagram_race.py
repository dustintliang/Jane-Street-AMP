import itertools

def basic_checks(word1:str, word2:str)-> tuple[bool, str, str]:
    '''Implements top-level checks common to each is_anagram approach. 
       Anagram basic checks include ensuring the two input words:
        -aren't be the same word
        -are case insensitive
        -don't include characters other than A-Z, a-z
        -have the same length, with at least two letters

       Args:
         word1: The first word
         word2: The second word

       Returns:
         bool: False if the two words fail a basic check, True otherwise
         str: A lowercase version of word1 only containing A-Z, a-z
         str: A lowercase version of word2 only containing A-Z, a-z
        
       Examples:
        >>> basic_checks("baste2", "Beast")
        True, baste, beast
        >>> basic_checks("baste", "Beasts")
        False, baste, beasts
    '''
    ### BEGIN SOLUTION
    valid_characters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word1 = word1.lower()
    word2 = word2.lower()
    for letter in word1:
        if letter not in valid_characters:
            word1 = word1.replace(letter,"")
    for letter in word2:
        if letter not in valid_characters:
            word2 = word2.replace(letter,"")
    if len(word1) <= 2 or len(word2) <= 2 or word1 == word2 or len(word1) != len(word2):
        return (False, word1, word2)
    else:
        return (True, word1, word2)
    ### END SOLUTION 

def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
        ### BEGIN SOLUTION
    validity, word1, word2 = basic_checks(word1, word2)
    if validity == False:
        return False
    for word in itertools.permutations(word1):
        test = ""
        for i in word:
            test += i
        if test == word2:
            return True
    return False
    ### END SOLUTION 
    ### END SOLUTION 

def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    valid_characters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word1 = word1.lower()
    word2 = word2.lower()
    list_2 = list()
    for letter in word1:
        if letter not in valid_characters:
            word1 = word1.replace(letter,"")
    for letter in word2:
        if letter not in valid_characters:
            word2 = word2.replace(letter,"")
        if letter in valid_characters:
            list_2.append(letter)
    if len(word1) <= 2 or len(word2) <= 2 or len(word1) != len(word2) or word1 == word2:
        return False
    for letter in word1:
        if letter in list_2:
            list_2.remove(letter)
    if len(list_2) == 0:
        return True
    else:
        return False
    ### END SOLUTION 

def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''Two approaches:
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. chr(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    validity, word1, word2 = basic_checks(word1, word2)
    if validity == False:
        return False
    
    for word in itertools.permutations(word1):
        test = ""
        for i in word:
            test += i
        print(test)
        if test == word2:
            return True
    return False
    ### END SOLUTION 

def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''Two approaches:
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. chr(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    validity, word1, word2 = basic_checks(word1, word2)
    if validity == False:
        return False
    dict1 = dict()
    dict2 = dict()
    for letter in word1:
        dict1[letter] = dict1.get(letter, 0)+1
    for letter in word2:
        dict2[letter] = dict2.get(letter, 0)+1
    if len(word1) <= 2 or len(word2) <= 2 or len(word1) != len(word2) or word1 == word2:
        return False
    for k,v in dict1.items():
        if k not in dict2.keys():
            return False
        if dict2[k] != v:
            return False
    return True
    ### END SOLUTION 

def is_anagram_sort_hash(word1:str, word2:str)->bool:
    '''Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    list_1 = list()
    list_2 = list()
    validity, word1, word2 = basic_checks(word1, word2)
    if validity == False:
        return False
    for i in word1:
        list_1.append(i)
    for i in word2:
        list_2.append(i)
    list_1.sort()
    list_2.sort()
    if len(word1) <= 2 or len(word2) <= 2 or len(word1) != len(word2) or word1 == word2:
        return False
    if list_1 == list_2:
        return True
    else:
        return False
    ### END SOLUTION 

ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def is_anagram_prime_hash(word1:str, word2:str)->bool:
    '''Create a dictionary of prime numbers (see chToprime above). Use the ascii value of each letter in both
      words to construct a unique numeric representation of the word (called a 'hash').
      Words with the same hash value are anagrams of each other.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    validity, word1, word2 = basic_checks(word1, word2)
    if validity == False:
        return False
    hash_value_1 = 1
    hash_value_2 = 1
    for letter in word1:
        hash_value_1 *= ch_to_prime[letter]
    for letter in word2:
        hash_value_2 *= ch_to_prime[letter]
    if hash_value_1 == hash_value_2:
        return True
    return False
    ### END SOLUTION 

if __name__ == "__main__":
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort_hash, is_anagram_prime_hash]
    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")