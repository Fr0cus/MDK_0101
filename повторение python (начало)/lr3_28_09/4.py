x = int(input())
y = str()
for i in range(5):
    y += str(x%10)
    x //= 10
print(y)