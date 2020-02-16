#1. 절댓값 구하기

def abs(a):
    if a >= 0:
        return a
    else:
        return a * -1

b = -97

print(abs(b))