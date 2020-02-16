#1. 정사각형, 직사각형의 넓이
#1.에서 a, b는 각각 가로, 세로이다.

def rectangle(a, b):
    return a * b

#2. 평행사변형의 넓이
#2.에서 a, b는 각각 밑변, 높이다.

def parallelogram(a, b):
    return a * b

#3. 삼각형의 넓이
#3.에서 a, b는 각각 밑변, 높이다.

def triangle(a, b):
    return a * b / 2

#4. 마름모의 넓이
#4.에서 a, b는 각각 한 대각선, 다른 대각선이다.

def diamond_shape(a, b):
    return a * b / 2

#5. 사다리꼴의 넓이
#5.에서 a, b, c는 각각 윗변, 아랫변, 높이다.

def trapezoid(a, b, c):
    return (a + b) * c / 2

#6. 원의 넓이
#6.에서 a는 반지름이다. 그리고 원주율은 3.14로 한다.

def circle(a):
    return a * a * 3.14

#7. 원의 둘레
#7.에서 a는 반지름이다. 그리고 원주율은 3.14로 한다.

def circumference(a):
    return a * 2 * 3.14

#8. 정육면체, 직육면체의 부피
#8.에서 a, b, c는 각각 가로, 세로, 높이다.

def rectangular_parallelepiped(a, b, c):
    return a * b * c

#9. 원기둥의 부피
#9에서 a, b는 각각 반지름, 높이다. 그리고 원주율은 3.14이다.

def cylinder(a, b):
    return a * a * 3.14 * b

print(rectangle(3, 8))
print(parallelogram(3, 8))
print(triangle(3, 8))
print(diamond_shape(3, 8))
print(trapezoid(2, 3, 5))
print(circle(3))
print(circumference(3))
print(rectangular_parallelepiped(2, 5, 7))
print(cylinder(4, 5))