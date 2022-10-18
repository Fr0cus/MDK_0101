a, p = int(input()), int(input())
SP = [a]
for i in range(1, 10):
    SP.append(a+i*p)
print(*SP)