def gcd(lst):
    lst.sort()
    target=1
    for k in range(lst[len(lst)-1], 0, -1):
        for i in range(len(lst)):
            if lst[i]%k!=0:
                target=0
                break
        if target:
            gcd=k
            break
        else:
            pass
        target=1
    return gcd
                
    
num = input("逗號分隔: ")
lst = num.split(",")
for i in range(len(lst)):
    lst[i] = eval(lst[i])
print(gcd(lst))

