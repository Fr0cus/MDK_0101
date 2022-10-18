with open(r'D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie3\\zadanie3.txt') as f:
    print(*(sum(map(int, line.split())) for line in f.readlines()), sep='\n')