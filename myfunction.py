# k = float(input("k의 값을 넣으시오. : "))
def add_all(k):
    number = []
    n = 0
    while n <= 100:
        number.append(pow(1/k, n))
        n = n + 1
    return sum(number)


for k in range(1, 1001):
    s = add_all(k)
    print(str(k) + ',' + str(s))

