
f=open('D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie7\\zadanie7.txt')  
f1=open('D:\\Code_all\\MDK_0101\\повторение python (начало)\\lr7_04_10\\zadanie7\\zadanie7a.txt','a')
b = f.readlines()
    
for word in (b):
    f1.write(word[::-1])


for worda in reversed(b):
    f1.write(worda[::-1])

f.close()
f1.close()

