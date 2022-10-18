n = int(input())
maxx = n%10
minn = n%10
k = 0
maxi = k
mini = k
while n>0:
    i =  n % 10
    k +=1
    if i >= maxx:
        maxx = i 
        maxi = k

    if i <= minn:
        minn = i
        mini = k

    n = n // 10

if maxi > mini:
    print('Максимум левее')
else:
    print('Минимум левее')

