def get_menu_choice()->list:
    """Prompts the use to enter a valid menu choice to indicate which sequence should be generated.
       Also prompts the user to enter how many terms they would like to see.

       Returns:
          A list consisting of two items:
            - the number of terms in the sequence
            - a single letter indicating the desired type of sequence 
    """
    print("Enter your choice:")
    print("-----------------")
    print("  (O)dd Integers")
    print("  (M)ultiples")
    print("  (S)quare numbers")
    print("  (T)riangular numbers")
    print("  (A)rithmetic Sequence")
    print("  (F)ibonacci Sequence")
    choice = input("Which sequence would you like to generate?\n")

    while choice.lower() not in ["o", "m", "s", "t", "a", "f"]:
        choice = input("Which sequence would you like to generate?\n")

    n = int(input("How many terms would you like to see?\n"))

    return [n, choice.lower()] 


def positive_odds(n: int)->list:
    """Returns a list of the first n positive odd integers.
        
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n positive odd numbers

        Example
        --------
        >>> positive_odds(4)
        [1, 3, 5, 7]
    """
    if n > 0:
      lst = list()
      for i in range(1, 1+2*(n), 2): #edited this line
          lst.append(i)
      return lst
    if n <= 0:
        false_lst = list()
        return false_lst

def positive_multiples(n: int, m: int)->list:
    """Returns a list of the first n positive integer multiples of m.
 
        Args:
          n: The number of terms in the sequence to generate
          m: The positive integer multiple 

        Returns:
          A list of n positive integer multiple of m

        Example
        --------
        >>> positive_multiples(4, 6)
        [6, 12, 18, 24]
    """
    if n > 0 and m > 0: #edited this line
        lst = list()
        for i in range(m, (n+1)*m, m):
            lst.append(i)
        return lst
    if n <= 0 or m <= 0: #edited this line
        false_lst = list()
        return false_lst
      
        


def square_numbers(n: int)->list:
    """Returns a list of the first n non-negative square integers.
 
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n square numbers
          
        Example
        --------
        >>> square_numbers(4)
        [0, 1, 4, 9]
    """
    lst = list()
    for number in range(n):
      square_number = number**2
      lst.append(square_number)
    return lst


def triangle_numbers(n: int)->list:
    """Returns a list of the first n triangle numbers.
 
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n triangle numbers
          
        Example
        --------
        >>> triangle_numbers(6)
        [1, 3, 6, 10, 15, 21]
    """
    #triangle_lst = list()
    #for i in range(1, n+1):
      #triangle_number = i**2-triangle_lst[i-1]
      #triangle_lst.append(triangle_number)
    #return triangle_lst
   
   #don't really get triangle numbers (somehow fixed code by randomly testing, but code is definitely not the best)
    lst = list()
    if n <= 0:
        return lst
    if n == 1:
        lst.append(int(1))
        return lst
    if n > 1:
        test_lst = range(1, n+1)
        for i in test_lst:
            if i == 1:
                lst.append(i)
            else:
                i = i**2 - lst[i-2]
                lst.append(i)
        return lst


def arithmetic_sequence(n: int, t1: int, t2: int)->list:
    """Returns a list of the first n terms of the arithmetic sequence defined by t1 and t2.
 
        Args:
          n: The number of terms in the sequence to generate
          t1: The first term in the sequence
          t2: The second term in the sequence

        Returns:
          A list of n terms in the arithmetic sequence defined by t1 and t2
          
        Example
        --------
        >>> arithmetic_sequence(4, 3, 7)
        [3, 7, 11, 15]
    """
    lst = list()
    for i in range(t1, t1+(t2-t1)*(n+1)-(t2-t1), (t2-t1)):
        lst.append(i)
    return lst


def fibonacci_sequence(n: int)->list:
    """Returns a list of the first n terms of the fibonacci sequence.
 
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n fibonnaci numbers
          
        Example
        --------
        >>> fibonacci_sequence(5)
        [1, 1, 2, 3, 5]
    """
    fib_lst = list()
    count = 0
    n1 = 1
    n2 = 1
    while count < n:
      fib_lst.append(n1)
      next_n = n1 + n2
      n1 = n2
      n2 = next_n
      count = count + 1
    return (fib_lst)



if __name__ == "__main__":
    n, choice = get_menu_choice()
  
    match choice:
        case "o":
            seq = positive_odds(n)
            label = "Positive Odd Integers"
        case "m":
            multiple = int(input("Which multiple would you like to use?"))
            seq = positive_multiples(n, multiple)
            label = "Positive Integer Multiples"
        case "s":
            seq = square_numbers(n)
            label = "Square Numbers"
        case "t":
            seq = triangle_numbers(n)
            label = "Triangle Numbers"
        case "a":
            term_1 = int(input("What is the first term of the arithmetic sequence?"))
            term_2 = int(input("What is the second term of the arithmetic sequence?"))
            seq = arithmetic_sequence(n, term_1, term_2)
            label = "Arithmetic Sequence"
        case  "f":
            seq = fibonacci_sequence(n)
            label = "Fibonacci Numbers"
        case _:
            seq = None

    print(f"The first {n} terms of the {label}: {seq}")
    