lst = list()
n1 = 1
n2 = 1
while n1 < 4000000:
    next_n = n1+n2
    if n1%2==0:
        lst.append(n1)
    n1 = n2
    n2 = next_n
sum = 0
for i in lst:
    sum += i
print(sum)