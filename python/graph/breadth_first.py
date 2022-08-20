from collections import deque # double-ended queue
import set_graph
# 廣度優先搜尋 O(V+E), vertrex,edge

graph = set_graph.setGraph()
# 搜尋條件
def condition(name):
    return name[-1]=='m'

def breadth_first_search(start):
    search_queue = deque()
    search_queue+=graph[start]
    done=[] # 是否已經檢查過，避免重複檢查
    while search_queue:
        data = search_queue.popleft()
        print(data)
        if data not in done:
            if condition(data):
                print(data, "is true!")
                return True
            else:
                search_queue+=graph[data] #和該節點有相鄰的節點放入queue中
                done.append(data) # 檢查過的節點加入done[]
        return False

breadth_first_search("you")
