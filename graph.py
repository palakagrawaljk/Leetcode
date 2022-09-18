edges=[[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
nodes=[0,1,2,3,4,5]


graph={}
distance={}
#represent edges and nodes of graph as matrix
for i in range(len(nodes)):
    graph[i]=[]
    distance[i]=None
#print(graph)

#connected
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
#print(graph)

def dfs(graph,node,visited):
    print(node)
    visited.add(node)
    sm=0
    for child in graph[node]:
        if child not in visited:
            sm+=dfs(graph,child,visited)
    return sm+1
#sm is no of elements we are able to traverse by a node using dfs approach          
#print(dfs(graph,1,visited=set()))

#no of connected components(families) needed to visit all nodes.
visited=set()
countArr=[]
for item in nodes:
    if item not in visited:
        temp=dfs(graph,item,visited)
        countArr.append(temp)
print(countArr)

#shortest path
def sssp(graph,node,distance,d,par):
    distance[node]=d
    for child in graph[node]:
        #to skip case, when it is undirected graph.
        if child!=par: 
            sssp(graph,child,distance,distance[node]+1,node)
            
start=0
distance[start]=0
sssp(graph,start,distance,0,-1)
for key,value in distance.items():
    print(key,value)