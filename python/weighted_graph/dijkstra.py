# 有向無環圖(Directed Acycle Graph, DAG)
# weight is positive
# 不能處理負權重邊的圖形 -> 需採用Bellman-Ford演算法[ O(V*E) ]

graph={}

# 相鄰節點
graph["start"]={}
graph["start"]["A"]=6
graph["start"]["B"]=2

graph["A"]={}
graph["A"]["fin"]=1

graph["B"]={}
graph["B"]["A"]=3
graph["B"]["fin"]=5

graph["fin"]={}

# 目前節點的成本
infinity=float("inf")
costs={}
costs["A"]=6
costs["B"]=2
costs["fin"]=infinity

# 目前節點的父節點
parents={}
parents["A"]="start"
parents["B"]="start"
parents["fin"]=None

# 已處理過的節點之List
processed=[]

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    
    for node in costs:
        cost = costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node=node
    return lowest_cost_node
    

def main():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node] # 與目前節點相鄰的所有節點
        for n in neighbors.keys():
            new_cost = cost+neighbors[n] # 新成本=原成本+到下一節點的成本
            if costs[n] > new_cost: # 若原先成本>新成本
                costs[n] = new_cost # 更新成本
                parents[n] = node # 更新父節點
        print(costs)
        processed.append(node) # 已處理完畢此節點
        node = find_lowest_cost_node(costs)
        
        
if __name__=='__main__':
    print("initial costs: ", costs)
    main()