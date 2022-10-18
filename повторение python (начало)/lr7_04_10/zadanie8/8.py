count = 0
eq = True
with open("D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie8\\zadanie8.txt", "r", encoding = "utf-8") as f1, open("D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie8\\zadanie8a.txt", "r", encoding = "utf-8") as f2:
    for a1, a2 in zip(f1, f2):
        count += 1
        if a1 != a2:
            eq = False
            break

if eq == True:
    print("Нет отличий")
else:
    print("Отличается строка ", count)
