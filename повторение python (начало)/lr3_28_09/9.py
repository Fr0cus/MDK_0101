n, f, s = int(input()), int(input()), int(input())
if s != 0:
    if n == f:
        print('Нет')
    else:
        if s<0:
            f= n
            n = f
            s = abs(s)
        while f<n:
            f += s
        if n==f:
            print("Да")
        else:
            print("Нет")
else:
    if n==f:
        print('Да')
    else:
        print('Нет')