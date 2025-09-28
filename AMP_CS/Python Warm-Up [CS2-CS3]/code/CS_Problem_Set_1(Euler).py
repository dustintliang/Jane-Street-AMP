# PE #7: Find the 10001st Prime
import math
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

def find_nth_prime(n: int) -> int:
    prime_list = list()
    if n == 1:
        return 2
    term = 2
    possible_prime = 3
    prime_list.append(2)
    while term <= n:
        if is_prime_factor_fold(possible_prime) == True:
            prime_list.append(possible_prime)
            term += 1
        possible_prime += 2
    return prime_list[-1]

print(find_nth_prime(10001))

'''
more efficient to do (lists didn't really help):
def find_nth_prime(n: int) -> int:
    if n == 1:
        return 2
    term = 2
    possible_prime = 3
    while term <= n:
        if is_prime_factor_fold(possible_prime) == True:
            term += 1
        possible_prime += 2
    possible_prime -= 2
    return possible_prime

print(find_nth_prime(10001))
'''

#PE #10: Summation of Primes
def sum_of_primes(max: int) -> int:
    #returns sum of primes lower than the max
    if max <= 2:
        return 0
    if max <= 3:
        return 2
    possible_prime = 3
    sum = 2
    while possible_prime < max:
        if is_prime_factor_fold(possible_prime) == True:
            sum += possible_prime
        possible_prime += 2
    return sum

print(sum_of_primes(2000000))