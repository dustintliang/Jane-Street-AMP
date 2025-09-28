import itertools
class AnagramExplorer:
    def __init__(self, all_words: list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.build_lookup_dict() # Only calculated once, when the explorer object is created

    @property
    def corpus(self):
      return self.__corpus

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str]) -> bool:
       '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)
            -are both at least 3 letters long (and the same)
            -form a valid anagram pair
            -consist entirely of letters chosen at the beginning of the game

            Args:
                pair (tuple): Two strings representing the guessed pair
                letters (list): A list of letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
       '''
        ### BEGIN SOLUTION
       if pair[0].lower() not in self.__corpus or pair[1].lower() not in self.__corpus or len(pair[0]) < 3 or len(pair[1]) < 3 or pair[0].lower() == pair[1].lower():
          return False
       letters1 = sorted(list(pair[0].lower()))
       letters2 = sorted(list(pair[1].lower()))
       if letters1 != letters2:
          return False
       for letter in letters1:
          if letters1.count(letter) > letters.count(letter):
             return False
          if letter not in letters:
             return False
       for letter in letters2:
          if letters2.count(letter) > letters.count(letter):
             return False
          if letter not in letters:
             return False
       return True
        ### END SOLUTION 
        
    def build_lookup_dict(self) -> dict:
        '''Creates a fast dictionary look-up (via either prime hash or sorted tuple) of all anagrams in a word corpus.
       
            Args:
                corpus (list): A list of words which should be considered

            Returns:
                dict: Returns a dictionary with  keys that return sorted lists of all anagrams of the key (per the corpus)
        '''
        ### BEGIN SOLUTION
        dictionary = dict()
        self.__corpus.sort()
        for word in self.__corpus:
          key = tuple(sorted(list(word)))
          dictionary[key] = dictionary.get(key, []) + [word]
        return dictionary
        ### END SOLUTION 

    def get_all_anagrams(self, letters: list[str]) -> set:
        '''Creates a set of all unique words that could have been used to form an anagram pair.
           Words which can't create any anagram pairs should not be included in the set.

            Ex)
            corpus: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
            all_anagrams: {"abed",  "abled", "baled", "bead", "blade"}

            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              set: all unique words in corpus which form at least 1 anagram pair
        '''
        ### BEGIN SOLUTION
        returned_set = set()
        n = 3
        while n <= len(letters):
         for k in itertools.combinations(letters, n):
               k = tuple(sorted(k))
               try:
                  if len(self.anagram_lookup[k]) >= 2:
                     returned_set.update(set(self.anagram_lookup[k]))
               except:
                  continue
         n += 1
        returned_set = set(sorted(returned_set))
        try:
           return returned_set
        except:
           return ""
        ### END SOLUTION 

    def get_most_anagrams(self, letters:list[str]) -> str:
      '''Returns any word from one of the largest lists of anagrams that 
         can be formed using the given letters.
         
         Args:
            letters (list): A list of letters from which the anagrams should be created

         Returns:
            str: a single word from the largest anagram families
      '''
      ### BEGIN SOLUTION
      n = 3
      largest_family_words = list()
      max_len = 1
      while n <= len(letters):
         for k in list(itertools.combinations(letters, n)):
               k = tuple(sorted(k))
               if k in self.anagram_lookup.keys():
                  if len(self.anagram_lookup[k]) > max_len:
                     largest_family_words = self.anagram_lookup[k]
                     max_len = len(self.anagram_lookup[k])
                  if len(self.anagram_lookup[k]) == max_len:
                     largest_family_words += self.anagram_lookup[k]
               else:
                  continue
         n += 1
      if len(largest_family_words) >= 2:
         return largest_family_words[0]
      else:
         return ''
        ### END SOLUTION 

if __name__ == "__main__":
  words1 = [
     "abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
     "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
     "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"
  ]
  words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]
  words3 = ['abed', 'mouse', 'bead', 'baled', 'abled', 'rat', 'blade']

  letters = ["l", "o", "t", "s", "r", "i", "a"]
  letters1 = ['a', 'b', 'e', 'd', 'l']

  my_explorer = AnagramExplorer(words3)

  #print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  #print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  #print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_most_anagrams(letters1))