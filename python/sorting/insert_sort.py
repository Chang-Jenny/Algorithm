def show(lst):
    # print outcome
    for i in range(0, len(lst)):
        print("%4d"%(int(lst[i])), end=" ")
    print()
    
def process(data):
    # deal user's data
    lst = data.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

def insert_sort(lst):
    # 適用於大多已排序好的情況
    for i in range(1, len(lst)):
        temp=lst[i] # current
        num = i-1 # comparison 
        """從目前的前一個開始相互比較
        1. 若目前數字較大則不動
        2. 若較小則依序往前面比較"""
        while num>=0 and temp<lst[num]:
            lst[num+1] = lst[num] # 前一個數字取代目前
            lst[num] = temp # 目前數字取代前一個數字
            num-=1 # 繼續往前檢查
    return lst
        
def main():
    # lst = list(map(int, input("請用空格分割數字: ").split()))
    data = input("請用空格分割數字: ")
    lst = process(data)
    print("Initial: ", end="")
    show(lst)
    lst = insert_sort(lst)
    print("After: ", end="")
    show(lst)
    
    
    
if __name__=='__main__':
    main()