#Тест 1
f = open('D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie10\\test1.txt', 'r', encoding='utf8')
#Тест 2
#f = open('D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie10\\test2.txt', 'r', encoding='utf8')
#Тест3
#f = open('D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie10\\test3.txt', 'r', encoding='utf8')
x = int(f.readline())
lines = f.readlines()
a = []
for line in lines:
    a.append(line.split())
g = []
for i in range(0, len(a)):
    if int(a[i][-1]) >= 40 and int(a[i][-2]) >= 40 and int(a[i][-3]) >= 40:
        g.append(int(a[i][-1]) + int(a[i][-2]) + int(a[i][-3]))
g.sort(reverse=True)
if len(g) <= x or x == 0:
    print(0)
else:
    if g.count(max(g)) > x:
        print(1)
    elif g.count(max(g)) == x:
        print(max(g))
    elif g.count(g[x - 1]) == 1:
        print(g[x - 1])
    elif g.count(g[x - 1]) > 1:
        i = 0
        while x - 1 - i >= 0:
            if g[x - 1 - i] != g[x - 1]:
                print(g[x - 1 - i])
                break
            else:
                i = i + 1
f.close()