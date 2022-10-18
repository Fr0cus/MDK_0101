x = int(input())
f = x % 100  #2
s = x % 10  #3
l = x //100 

print(l*100 +f//10 + s*10)