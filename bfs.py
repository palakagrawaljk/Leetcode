def bfs(graph,visited):
    queue=[]
    queue.append(1)
    visited.add(1)
    while queue:
        ele=queue.pop()
        print(ele)
        if ele in graph:
            for child in graph[ele]:
                if child not in visited:
                    queue.append(child) 

graph={1:[2,3],2:[5,6],}
visited=set()
bfs(graph,visited)