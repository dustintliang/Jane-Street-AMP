import math
import itertools
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

def prime_permutations_same_difference(digits: int) -> int:
    soln = ''
    #finding primes
    for number in range(10**(digits-1)+1, 10**digits, 2):
        soln_list = []
        if '0' in list(str(number)):
            continue
        prime = True
        for prime_tester in range(2, int(math.sqrt(number)+1)):
            if number % prime_tester == 0:
                prime = False
        #finding permutations of the prime
        if prime == True:
            for permutation in itertools.permutations(str(number), digits):
                soln_list.append(permutation)
            soln_list.sort()
            #finding combinations of 3
            for combo in itertools.combinations(soln_list, 3):
                if combo[0] == combo[1] or combo[1] == combo[2] or combo[0] == combo[2]:
                    continue
                list2 = []
                for number in combo:
                    tuple_remover = ''
                    for digit in number: 
                        tuple_remover += digit
                    list2.append(tuple_remover)
                list2.sort()
                #making sure the combinations of 3 satisfy conditions
                if is_prime_factor_fold(int(list2[0])) == False or is_prime_factor_fold(int(list2[1])) == False or is_prime_factor_fold(int(list2[2])) == False:
                    continue
                if int(list2[1])-int(list2[0]) == int(list2[2])-int(list2[1]):
                    soln = list2[0]+list2[1]+list2[2]
                    if int(soln) != 148748178147:
                        return soln
print(prime_permutations_same_difference(4))

def permuted_multiples(max: int):
    permuted = False
    x = 1
    while permuted == False:
        correct = 0
        for multiplier in range(2, max):
            if list(sorted(str(multiplier*x))) != list(sorted(str((multiplier+1)*x))):
                x += 1
                break
            else:
                correct += 1
        if correct == max-2:
            permuted = True
    return x
print(permuted_multiples(6))