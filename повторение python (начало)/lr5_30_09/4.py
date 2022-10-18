def f1(x):
    a = min(x)
    b = max(x)
    average = sum(x)/len(x)
    ave = round(average, 3)
    return a, b, ave
 
def f2(*x):
    a = min(x)
    b = max(x)
    average = sum(x)/len(x)
    ave = round(average, 3)
    return a, b, ave
 
x = [-39, -62, 63, -84, -9, 59, -33, -2, 99, -19, 8, 79, -70, -8, 71, 31, 26, 45, -20]
print(f1(x))
print(f2(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18]))