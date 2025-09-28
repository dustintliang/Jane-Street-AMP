#number must be X X X X X X
p_list = list()
list_1 = range(999, 99, -1)
list_2 = range(999, 99, -1)
for number_1 in list_1:
    for number_2 in list_2:
        six_digit = str(number_1*number_2)
        if len(six_digit) < 6:
            break
        if six_digit[0] == six_digit[5] and six_digit[1] == six_digit[4] and six_digit[2] == six_digit[3]:
            p_list.append(int(six_digit))
            break
p_list.sort(reverse=True)
print(p_list[0])