with open(r"D:\\Code_all\\MDK_0101\\практические_работы1\\pr3_05_10\\zadanie2.txt") as f:
    n = f.read()
    f.close()
    x = input()
    #    O(n)
    for i in n:
        #   O(1)
        if(i == x):
            print("Yes")
            # O(1)
            break