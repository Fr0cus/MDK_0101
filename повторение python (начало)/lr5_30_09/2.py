import math 

def f(x, y):
    a = math.cos(x) + y -1.5
    b = 2*x - math.sin(y - 0.5) - 1
    return a, b

x, y = int(input()), int(input())
print(f(x,y))