#1. 곱셈을 쉽게 하는 방법

def multiply(a, b):
    return a * b

#2. 곱셈을 쉽게 하지 않고 아주 힘들게 오래 계산하는 방법

def multiply_in_add(a, b):
    i = 0
    c = 0
    if b > a:
        s = a
        a = b
        b = s

    while i < b:
        i = i + 1
        c = c + a
    return c


print(multiply(29494, 111111488))
print(multiply_in_add(29394858, 193274838))