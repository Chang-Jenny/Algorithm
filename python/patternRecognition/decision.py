import math
import pandas as pd
import numpy as np
import csv

# ID3
# https://iter01.com/127943.html

# Read file, initial variable
def init():
    dataSet=[]
    # customer = pd.read_csv('customer.csv', sep=';')
    with open('customer.csv', 'r', newline="") as f:
        for data in csv.reader(f):
            dataSet.append(data)
    # print(dataSet)
    dataNum = len(dataSet)-1 # data length
    return dataSet

# calculate Info(D)
def calEntropy(dataSet):
    info=0.0
    dictCount={}
    for i in range(1,len(dataSet)):
        if dataSet[i][-1] not in dictCount.keys():
            dictCount.setdefault(dataSet[i][-1], 0)
        dictCount[dataSet[i][-1]]+=1
    # print(dictCount)
    
    for i in dictCount.keys():
        dictCount[i]
        info+=(-1)*(dictCount[i]/(len(dataSet)-1))*(math.log2(dictCount[i]/(len(dataSet)-1)))
    print("Info(D) = %.4f bits"%(info))
    
# split dataSet
def splitDataSet(dataSet):
    print("split")
    
# calculate InfoAttri(D)
def calGain():
    print("gain")

calEntropy(init())

    
    