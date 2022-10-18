# Числа через пробел
x = [int(i) for i in input().split()]
kolvo = 1
for i in range(0, len(x) - 1):
    if x[i] != x[i + 1]:
        kolvo += 1
print(kolvo)