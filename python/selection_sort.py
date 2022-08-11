# find the smallest number and its index
def find_smallest_index(lst):
    smallest_item=lst[0]
    smallest_index=0
    
    for i in range(1, len(lst)):
        if lst[i] < smallest_item:
            smallest_index = i
            smallest_item = lst[i]
    return smallest_index

# sort
def selection_sort(lst):
    new_lst=[]
    for i in range (len(lst)):
        smallest_index = find_smallest_index(lst)
        new_lst.append(lst.pop(smallest_index))
        print(new_lst)
    return new_lst

# lst = [5,4,3,2,1]
# print(selection_sort(lst))