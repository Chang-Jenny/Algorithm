def MergeSort(lst):
    if len(lst) <2:
        return lst
    
    mid = len(lst)//2
    leftLst=lst[:mid]
    rightLst=lst[mid:]
    return Merge(MergeSort(leftLst), MergeSort(rightLst))

def Merge(leftLst, rightLst):
    outcome=[]

    while len(leftLst) and len(rightLst):
        if (leftLst[0] < rightLst[0]):
            outcome.append(leftLst.pop(0))
        else:
            outcome.append(rightLst.pop(0))
    # 剩餘的再直接放入result，因為已經排序好了
    # outcome = outcome+leftLst if len(leftLst) else outcome+rightLst
    if len(leftLst):
        outcome+=leftLst 
    else:
        outcome+=rightLst
    print(outcome)
    return outcome


data = list(map(int, input("請以空白鍵分隔數字: ").split()))
print(MergeSort(data))