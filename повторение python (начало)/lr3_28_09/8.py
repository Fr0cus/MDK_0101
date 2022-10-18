n = int(input())
m=0
c = 0
for i in range(len(str(n))+1):
    k=n%10
    if k>m: 
        m=k
        n=n//10
    if k==m: 
        c+=1
        n=n//10
print(c)