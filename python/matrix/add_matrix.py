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

def main():
    ary1=inputData()
    ary2=inputData()
    ary3=[]
    for i in range(row):
        ary3.append([])
        for j in range(col):
            ary3[i].append(ary1[i][j]+ary2[i][j])
            
    print(ary3)
    
if __name__=='__main__':
    main()