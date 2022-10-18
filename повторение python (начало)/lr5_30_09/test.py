def f(n):
    if (n==1):
        return "Нет"
    elif (n==2):
        return "Да"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "Нет"
        return "Да"             
print(f(int(input("Введите число: "))))
