row=eval(input("Rows: "))
col=eval(input("Cols: "))
def inputData():
    lst=[]
    for i in range(row):
        lst.append([])
        for j in range(col):
            lst[i].append(eval(input("[%d %d]= "%(i+1, j+1))))
    print()
    return lst

def trans(lst):
    outcome=[]
    for i in range(len(lst)):
        outcome.append([])
        for j in range(len(lst[i])):
            outcome[i].append(lst[j][i])
    return outcome

def main():
    lst = inputData()
    print(lst)
    outcome = trans(lst)
    for i in range(len(outcome)):
        for j in range(len(outcome[i])):
            print(outcome[i][j], end="  ")
        print()
          
if __name__=='__main__':
    main()