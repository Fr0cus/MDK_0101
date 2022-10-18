def sum(x):
    res = 0
    while x:
        res += x%10
        x //= 10
    return res

a = int(input())
b = int(input())

if sum(a)>sum(b):
    print(a)
elif sum(a)<sum(b):
    print(b)
else:
    print("Суммы равны")