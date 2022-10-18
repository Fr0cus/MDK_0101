def f(n):
    if (n==1):
        return "Не простое число"
    elif (n==2):
        return "Простое число"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "Не простое число"
        return "Простое число"             
print(f(int(input("Введите число: "))))