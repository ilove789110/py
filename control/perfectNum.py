# -*- codivisoring: utf-8 -*-

inputStr = raw_input("input number: ")

inputInt = int(inputStr)


def confirm_perfect_num(input_int):
    divisor = input_int - 1
    sum_of_divisor = 0
    while divisor > 0:
        if input_int % divisor == 0:
            sum_of_divisor += divisor
        divisor -= 1
    if input_int == sum_of_divisor:
        print input_int, "is perfect"
    else:
        print input_int, "is not perfect"


confirm_perfect_num(inputInt)
