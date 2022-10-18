n = int(input('Введите общее количество покупок: '))
a = {}
for i in range(n):
    shopin = input()
    f, tovar, amount = shopin.rsplit(maxsplit=3)
    amount = int(amount)
    if f not in a:
        a[f] = {tovar: amount}
    else:
        if tovar not in a[f]:
            a[f] |= {tovar: amount}
        else:
            a[f][tovar] += amount
for f, shopin in sorted(a.items()):
    print(f'{f}:')
    for tovar, amount in sorted(shopin.items()):
        print(tovar, amount)