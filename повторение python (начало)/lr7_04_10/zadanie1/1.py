with open(r"D:\\Code_all\\MDK_0101\\повторение python (Начало)\\lr7_04_10\\zadanie1\\zadanie1.txt") as datfile:
    text = datfile.read()
    print(sum(map(int, text.split(None, 2)[:2])))