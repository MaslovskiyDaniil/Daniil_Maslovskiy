num = int(input())
if num > 0:
    first_digit = num % 10
    second_digit = ((num // 10) % 10)
    if second_digit != 0:
        reversed_num = (first_digit * 10) + second_digit
        third_digit = num // 100
        if third_digit != 0:
            reversed_num = (reversed_num * 10) + third_digit
if num < 0:
    num //= -1
    first_digit = num % 10
    second_digit = ((num // 10) % 10)
    if second_digit != 0:
        reversed_num = (first_digit * 10) + second_digit
        third_digit = num // 100
        if third_digit != 0:
            reversed_num = ((reversed_num * 10) + third_digit) // -1
if  reversed_num > -2**7 and reversed_num < 2**7:
    print(reversed_num)
else:
    print('no solution')

