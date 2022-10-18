import math

def f(x: float) -> float:
    return x ** 3 * math.sin(x) - 0.985*x-0.991

print('y=', f(float(input())))