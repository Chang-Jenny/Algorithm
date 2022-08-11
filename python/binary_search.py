def binary_search(lst, item):
    low=0
    high=len(lst)-1
    
    while(low <= high):
        mid=(low + high)//2
        choose = lst[mid]
        print("Now choosing: lst[%d]=%d"%(mid, choose))
        if choose == item:
            return mid
        elif choose > item:
            high = mid-1
        else:
            low = mid+1
    return None

# lst = [1,3,5,7,9,11]
# print(binary__search(lst, 3))
