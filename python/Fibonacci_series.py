def fib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input("輸入要計算第幾個費氏數列: "))
for i in range(n+1):
    print("fib(%d)=%d"%(i, fib(i)))
