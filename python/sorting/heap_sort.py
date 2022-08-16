# https://ithelp.ithome.com.tw/articles/10279239
def Adjust_Max_Heap(lst, n,i):
    largest = i # root

    l = 2*i+1
    r = 2*i+2
    if l<n and lst[i] < lst[l]:
        largest=l
    if r<n and lst[largest]<lst[r]:
        largest=r
    if largest!=i:
        lst[i], lst[largest] = lst[largest], lst[i]
        Adjust_Max_Heap(lst, n,largest)

def HeapSort(lst):
    n = len(lst)
    
    for i in range(n//2-1, -1, -1):
        Adjust_Max_Heap(lst, n,i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        Adjust_Max_Heap(lst, i, 0)
data = list(map(int, input("請以空白鍵分隔數字: ").split()))
HeapSort(data)
print(data)