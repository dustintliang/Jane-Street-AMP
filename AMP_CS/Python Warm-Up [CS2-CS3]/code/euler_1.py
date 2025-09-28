sum = 0
lst = [x for x in range(1, 1000) if x%3==0 or x%5==0]
for i in lst:
    sum += i
print(sum)