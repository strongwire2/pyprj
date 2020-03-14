#1. a의 b승 구하는 방법

def 승(a, b):
    c = 1
    while b > 0:
        c = a * c
        b = b - 1
    return c


print(승(234, 10000))