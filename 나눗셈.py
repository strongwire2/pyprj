#1. 쉽게 하는 방법

def divide(a, b):
    return a / b

#2. 어렵고 내림해서 뺄셈으로 나눗셈 하는 방법

def if_you_want_to_do_it_in_a_hard_way(a, b):
    i = 0
    while a >= b:
        a = a - b
        i = i + 1
    return i


print(divide(4, 2))
print(if_you_want_to_do_it_in_a_hard_way(6, 2))