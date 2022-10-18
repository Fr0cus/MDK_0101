soiz = set()
vse = set()
for i in range(int(input())):
    a = int(input())
    b = {input() for j in range(a)}
    vse.update(b)
    if i == 1:
        soiz.update(b)
    else:
        soiz &= b
print(len(soiz))
print('\n'.join(sorted(soiz)))
print(len(vse))
print('\n'.join(sorted(vse)))