from unicodedata import category
import numpy as np

# 讀取檔案及座標
def gainData():
    x=[]
    y=[]
    file = open("position.txt", "r")
    k = file.readline()
    count=0
    pos = file.readline()
    while pos!="":
        pos = pos.strip().split(",")
        x.append(eval(pos[0]))
        y.append(eval(pos[1]))
        count+=1
        pos = file.readline()
    return k, count, x, y
    
# 歐式距離
def dist(x, y, kx, ky):
    distance = ((x-kx)**2+(y-ky)**2)**0.5
    # distance = round(distance, 2)
    distance = round(distance, 1)
    return distance
# 分群
def cluster(x, y, kx, ky):
    category=[]
    for i in range(0, len(kx)):
        category.append([])
    for i in range(0, len(x)): # 每個點都要和三個中心點計算距離
        tempLong=[]
        for j in range(0, len(kx)): # 三個中心點
            tempLong.append(dist(x[i], y[i], kx[j], ky[j]))
            
        which = tempLong.index(min(tempLong)) # 找最小的距離
        category[which].append([x[i], y[i]])
    return category

def calCenter(category):
    kx=[]
    ky=[]
    for index, nodes in enumerate(category):
        x=0
        y=0
        for i in range(0, len(nodes)):
            x+=category[index][i][0]
            y+=category[index][i][1]
        kx.append(round(x/len(nodes), 1))
        ky.append(round(y/len(nodes), 1))
        
    return kx, ky
    
    
def KMEANS(centerx, centery, flag): 
    category = cluster(gainData()[2], gainData()[3], centerx, centery)
    kx, ky = calCenter(category)
    
    # 列印過程
    print("第%d次: "%(flag))
    for i in range(len(centerx)):
        print(category[i])
    print("本次中心點: ")
    for i in range(len(kx)):
        print("[%.1f, %.1f]"%(kx[i], ky[i]))
    print("==================================================")
    
    # 判斷中心點不改變
    if(centerx==kx and centery==ky):
        print("次數：", flag)
        for i in range(len(kx)):
            print("中心點: [%.1f, %.1f]"%(kx[i], ky[i]))
        return
    else:
        flag+=1
        KMEANS(kx, ky, flag)
    
    

if __name__=='__main__':
    # 初始中心點
    centerx=[]
    centery=[]
    for i in range(0, eval(gainData()[0])):
        centerx.append(gainData()[2][i])
        centery.append(gainData()[3][i])
        
    KMEANS(centerx, centery, flag=0)


