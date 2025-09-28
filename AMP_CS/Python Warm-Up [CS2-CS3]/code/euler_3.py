import math
num = input("enter an integer:")
if float(num) % 1 != 0:
    print("try again")
num = int(num)

#find factors
test_lst = range(1, int(math.sqrt(num)+1))
small_lst = list()
for x in test_lst:
    if num%x==0:
        small_lst.append(x)
big_lst = list()
for x in small_lst:
    big_lst.append(int(num/x))
for x in big_lst[::-1]:
    if x not in small_lst:
        small_lst.append(x)


#check for prime
def prime_check(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

small_lst.reverse()
for i in small_lst:
    if prime_check(i) == True:
        print(i)
        break