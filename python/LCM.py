num = input("逗號分隔: ")
number = num.split(",")

for i in range(len(number)):
    number[i] = int(number[i])
    
number.sort()
target = number[-1]

while True:
    isRight=True
    for i in range(0, len(number)-1):
        if target%number[i]!=0:
            isRight=False
            break
    if isRight:
        break
    else:
        target=target+number[-1]
        # print(target)
    
print(target)
        