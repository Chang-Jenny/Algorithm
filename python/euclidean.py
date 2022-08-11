def euclidean(num1, num2):
    # 被除數和除數互換
    # 除數等於餘數
    if(num1<num2):
        t=num1
        num1=num2
        num2=t
    while(num2!=0):
        t=num1%num2
        num1=num2
        num2=t
    return num1

num_1 = int(input())
num_2 = int(input())
print("gcd(%d, %d)=%d"%(num_1, num_2, euclidean(num_1, num_2)))