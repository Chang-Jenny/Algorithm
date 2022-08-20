# 有向無環圖(Directed Acycle Graph, DAG)
# weight is positive
# 不能處理負權重邊的圖形 -> 需採用Bellman-Ford演算法[ O(V*E) ]


graph={}

# 相鄰節點
graph["start"]={}
graph["start"]["A"]=6
graph["start"]["B"]=2
# print(graph["start"]["a"])
graph["A"]={}
graph["A"]["fin"]=1

graph["B"]={}
graph["B"]["A"]=3
graph["B"]["fin"]=5

graph["fin"]={}

# 每個節點的成本
infinity=float("inf")
cost={}
cost["A"]=6
cost["B"]=2
cost["fin"]=infinity

# 父節點
parents={}
parents["A"]="start"
parents["B"]="start"
parents["fin"]=None
processed={}