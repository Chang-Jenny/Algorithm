def bubble_sort(lst):
    # 前後相比，若前者>後者則交換位置
    # 依序往下
    print("initial:", end=" ")
    for i in range(0, len(lst)):
        print("%4d"%(lst[i]), end=" ")
    print()
    
    for i in range(len(lst)-1, -1, -1):
    # for i in range(len(lst)-1, 0, -1): 有無自己與自己相比較的最後一次
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print("第%d次: "%(len(lst)-i), end=" ")
        for k in range(0, len(lst)):
            print("%4d"%(lst[k]), end=" ")
        print()
        
    print("outcome:", end=" ")
    for i in range(0, len(lst)):
        print("%4d"%(lst[i]), end=" ")
        

lst=list(map(int, input("Please input some number: ").split()))
bubble_sort(lst)

""" For Example: [5, 4, 3, 2, 1]
第1次:     4    3    2    1    5
第2次:     3    2    1    4    5
第3次:     2    1    3    4    5
第4次:     1    2    3    4    5
第5次:     1    2    3    4    5
"""
