# recursive版本
def QuickSort(lst):
    n=len(lst)
    if n <=1:
        return lst
    left=[]
    right=[]
    pivot=lst[0]

    for i in range(1, n):
        if lst[i] <= pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return QuickSort(left) + [pivot] + QuickSort(right)

data = list(map(int, input("請以空白鍵分隔數字: ").split()))
print(QuickSort(data))