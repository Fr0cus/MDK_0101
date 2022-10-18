from random import randint

boots = [randint(40, 47) for i in range(11)]
f40, f41, f42, f43, f44, f45, f46 = int(), int(), int(),int(),int(),int(),int()
for i in range(11):
    if boots[i] == 40:
        f40 = f40 + 1
    elif boots[i] == 41:
        f41 = f41 + 1
    elif boots[i] == 42:
        f42 = f42 + 1
    elif boots[i] == 43:
        f43 = f43 + 1
    elif boots[i] == 44:
        f44 = f44 + 1
    elif boots[i] == 45:
        f45 = f45 + 1
    elif boots[i] == 46:
        f46 = f46 + 1
print("Нужно обуви 40 размера"+ ":" + str(f40) , "Нужно обуви 41 размера"+ ":" + str(f41) , "Нужно обуви 42 размера"+ ":" + str(f42), "Нужно обуви 43 размера"+ ":" + str(f43), "Нужно обуви 44 размера"+ ":" +str(f44), "Нужно обуви 45 размера"+ ":" + str(f45), "Нужно обуви 46 размера"+ ":" + str(f46), sep="\n")
print ( boots, '- вот такие размеры нужно купить для футбольной команде.')
