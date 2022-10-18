#print(len(set(input().split())))
#print(len(set([int(i) for i in input().split()])))
a = set()

st=input()

for x in st:

    if '0' <= x <= '9' and x not in a: 
        a.add(x)

if len(a)>0:
    b=sorted(list(a))
    print(*b,sep='')
