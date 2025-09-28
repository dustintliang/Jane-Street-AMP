import math
def get_factors(n: int) -> list[int]:
    '''Generates a sorted list of unique integer factors for a given natural number

        Args:
            n (int): The natural number which should be factored

        Returns:
            list: a list of unique integer factors in sorted order

        Examples:
            >>> get_factors(6)
            [1, 2, 3, 6]
            >>> get_factors(17)
            [1, 17]
            >>> get_factors(36)
            [1, 2, 3, 4, 6, 9, 12, 18, 36]
            >>> get_factors(-2)
            []
    '''
    ### BEGIN SOLUTION
    big_lst = list()
    small_lst = list()
    if n <= 0:
        return big_lst
    else:
        for i in range(1, int(math.sqrt(n)+1)):
            if n%i == 0:
                big_lst.append(n//i)
                small_lst.append(i)
        for i in big_lst[::-1]:
            if i not in small_lst:
                small_lst.append(i)
    return small_lst
    ### END SOLUTION

def is_prime(n: int) -> bool:
    '''Determines whether a given integer is prime

       Args:
            n (int): The integer which should be tested

       Returns:
            bool: True if n is prime, False if n is not prime

       Examples:
            >>> is_prime(6)
            False
            >>> is_prime(11)
            True
    '''
    ### BEGIN SOLUTION
    if n <= 1:
        return False
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result
            

    ### END SOLUTION 

def largest_prime_factor(n: int) -> int:
    '''Determines the largest prime factor of a given whole number > 1.

       Args:
            n (int): The whole number which should be considered

       Returns:
            int: The largest prime factor of n
                 If the given integer isn't a whole number > 1, returns 0

       Examples:
            >>> largest_prime_factor(6)
            3
            >>> largest_prime_factor(100)
            5
    '''
    ### BEGIN SOLUTION
    if float(n) <= 1 or float(n) % 1 != 0:
        return 0
    

    rlist = list()
    lst = get_factors(n)
    lst.reverse()
    for i in lst:
        if is_prime(i) == True:
            return i
        
    ### END SOLUTION 

if __name__ == "__main__":
    #print("get_factors(25): ", get_factors(12))
    #print("is_prime(17): ", is_prime(12))
    print("largest_prime_factor(35): ", largest_prime_factor(97))
    print("largest_prime_factor(35): ", largest_prime_factor(2))
    print("largest_prime_factor(35): ", largest_prime_factor(155))
    print("largest_prime_factor(35): ", largest_prime_factor(6889))
    print("largest_prime_factor(35): ", largest_prime_factor(0))
    print("largest_prime_factor(35): ", largest_prime_factor(-17))
    print("largest_prime_factor(35): ", largest_prime_factor(1))
    print("largest_prime_factor(35): ", largest_prime_factor(90005673681))
    print("largest_prime_factor(35): ", largest_prime_factor(1387488001))