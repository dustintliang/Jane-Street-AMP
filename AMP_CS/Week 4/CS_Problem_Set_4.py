import math
from valid_ladders_word_list import get_valid_word_list

def Q2():
  def hamming_distance(w1:str, w2:str)-> int:
    if len(w1) != len(w2):
        return -1
    hamming_dist = 0
    for pos in range(len(w1)):
        if w1.lower()[pos] != w2.lower()[pos]:
            hamming_dist += 1
    return hamming_dist
  
  aloof_count = 0
  for word1 in get_valid_word_list():
      aloof = True
      for word2 in get_valid_word_list():
            if hamming_distance(word1, word2) == 1:
                aloof = False
                break
      if aloof == True:
          aloof_count += 1
  print(aloof_count)

def Q3():
  four_letter_word_list = list()
  for word in get_valid_word_list():
      if len(word) == 4:
          four_letter_word_list.append(word)

  def hamming_distance(w1:str, w2:str)-> int:
    if len(w1) != len(w2):
          return -1
    hamming_dist = 0
    for pos in range(len(w1)):
        if w1.lower()[pos] != w2.lower()[pos]:
            hamming_dist += 1
    return hamming_dist

  def build_adj_list(word_list: list[str])-> dict[str, set[str]]:
    adj_list = dict()
    for word1 in word_list:
        if word1.lower() not in adj_list:
          adj_list[word1.lower()] = set()
        for word2 in word_list:
            if word2.lower() not in adj_list:
                adj_list[word2.lower()] = set()
            if hamming_distance(word1, word2) == 1:
                adj_list[word1.lower()].add(word2.lower())
                adj_list[word2.lower()].add(word1.lower())
    return adj_list

  aloof_included = len(four_letter_word_list)**2
  adj_list = build_adj_list(four_letter_word_list)

  matrix = 0
  row_count = 0
  max_row = 0
  adj_elements = 0
  for k,v in adj_list.items():
      row_count += 1
      if len(v)>max_row:
          max_row = len(v)
      adj_elements += len(v)
  matrix_elements = row_count*max_row
  print(f'matrix elements: {aloof_included}, pruned matrix elements: {matrix_elements}, adjacency list elements: {adj_elements}')

def is_prime_factor_fold(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def Q5():  
  count = 0
  for i in range(2, 5000):
      if is_prime_factor_fold(i) == True:
          count += 1
  st = str(2**count)
  stl = list(st)
  print(len(stl))

Q2()
Q3()
Q5()