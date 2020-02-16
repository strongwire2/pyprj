#1. 배수를 구하는 방법 (작은 것 부터 5개)

def dominator(a):
    list = []
    i = 0
    c = 0
    while i < 5:
        i = i + 1
        c = c + a
        list.append(c)
    return list


list = dominator(10)

print(list)

