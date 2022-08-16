# D.L. Shell
# 謝耳排序法
# 將原始資料區分成特定間隔的小區塊，在小區塊中完成insert sort，依序降低間隔大小
# 減少insort sort資料搬移次數

def show(lst):
    # print outcome
    for i in range(0, len(lst)):
        print("%4d"%(int(lst[i])), end=" ")
    print()

def shell(lst):
    Y = len(lst)//2
    print(Y)
    while Y > 0:
        for i in range(Y, len(lst)):
            temp = lst[i]
            num = i-Y
            while num>=0 and temp<lst[num]:
                lst[num+Y]=lst[num]
                lst[num]=temp
                num-=Y
                # show(lst)
        show(lst)
        Y = Y//2
        
lst = list(map(int, input("請用空格分割數字: ").split()))
print("Initial: ",end="")
show(lst)
shell(lst)
            
        