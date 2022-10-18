a = []  
n = int(input())  
if n % 2 != 0:
    print('поменять местами нельзя')
else:
    for i in range(n):
        new_element = int(input())  
        a.append(new_element) 
    
    print(a)
    print(a[n // 2:] + a[0: n // 2])
