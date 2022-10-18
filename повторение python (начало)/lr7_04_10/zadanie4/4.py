file = open(r'D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie4\\zadanie4.txt')

lines = 0
words = 0
symbols = 0

for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line.strip('\n'))

print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)