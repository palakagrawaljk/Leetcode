#edges=[[1,2],[2,4],[4,3],[3,1],[2,5],[4,5]]
edges=[[1,2],[2,3],[3,6],[6,5],[5,4],[1,4]]

n=6
color={}
graph={}
visited=set()

#represent edges and nodes of graph as matrix
for i in range(1,n+1):
    graph[i]=[]
    color[i]=None
#print(graph)

#connected
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
print(graph)

#bipartite graph - graph in which alternate vertices have opposite colors(0/1)[we can break graph such that alternate vertices have opp colors]
def bipartite(graph,node,visited,color,c):
    visited.add(node)
    color[node]=c
    for child in graph[node]:
        if child not in visited:
            temp=bipartite(graph,child,visited,color,c^1)
            if temp==False:
                return False
        else:
            if(color[node]==color[child]):
                return False
    temp=True
    return temp

temp=bipartite(graph,1,visited,color,0)
print(temp)
'''
C:\Users\palagraw\Downloads\Leetcode>python bipartite.py
{1: [2, 3], 2: [1, 4, 5], 3: [4, 1], 4: [2, 3, 5], 5: [2, 4], 6: []}
False

C:\Users\palagraw\Downloads\Leetcode>python bipartite.py
{1: [2, 4], 2: [1, 3], 3: [2, 6], 4: [5, 1], 5: [6, 4], 6: [3, 5]}
True
'''
