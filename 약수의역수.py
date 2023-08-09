# n의 진약수를 리스트에 담아 리턴한다.
def get_divisor(n):
    d = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            d.append(i)
    return d


# 완전수, 부족수, 과잉수를 판단함.
def determine(d):
    # d = get_divisor(n)
    # 완전수 = 모든 약수를 더했을 때, 그 수의 2배가 되는 경우 = 모든 진약수를 더했을 때, 그 수가 되는 경우
    sum = 0
    for i in d:
        sum += i
    # print(f"sum={sum}, d[-1]={d[-1]}")
    if sum == d[-1]*2:
        return "완전수"
    elif sum < d[-1]*2:
        return "부족수"
    else:
        return "과잉수"


# max 까지의 수 중에서 완전수, 과잉수, 부족수의 개수를 계산함
def count(max):
    perfect = 0
    deficient = 0
    abundant = 0
    for i in range(1, max+1, 1):
        det = determine(i)
        if det == "완전수":
            perfect += 1
        elif det == "부족수":
            deficient += 1
        else:
            abundant += 1
        print(f"전체={i}, 완전수={perfect}({perfect*100/i}%), 부족수={deficient}({deficient*100/i}%), 과잉수={abundant}({abundant*100/i}%)")

# 주어진 수 n의 약수의 역수의 합을 구한다. CSV 형식으로 출력
def sum_of_inv(n):
    d = get_divisor(n)
    det = determine(d)
    sum = 0
    for i in d:
        sum += 1.0/float(i)
    print(f"{n}, {det}, {sum}")

if __name__ == '__main__':
    # print(get_divisor(16))
    # print(determine(get_divisor(6)))

    # count(100000)

    #
    for i in range(1, 100000+1):
        sum_of_inv(i)
