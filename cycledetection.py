#edges=[[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
edges=[[1,2],[1,3],[2,3],[2,4],[4,5],[5,1]]
nodes=[1,2,3,4,5]

graph={}
visited=set()
#represent edges and nodes of graph as matrix
for i in nodes:
    graph[i]=[]
print(graph)

#connected
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

def hasCycle(graph,node,visited,parent):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            return hasCycle(graph,child,visited,node)
        else:
            if child != parent:
                return True
    return False

temp=hasCycle(graph,1,visited,-1)
print(temp)