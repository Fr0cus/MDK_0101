n = int(input())
a=1
c=0
for i in range(1, n+1):
    b = 0
    b=a
    a=b+c
    c=b
    if b > n:
        print(b)
        break