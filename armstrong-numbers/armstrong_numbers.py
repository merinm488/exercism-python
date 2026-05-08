def is_armstrong_number(number):
    str_num = str(number)
    length = len(str_num)
    total = 0
    for i in range (0,length):
        total += int(str_num[i])**length
    return number == total

