def DFS(startNode,numberNodes,graph):
    visited=[False]*numberNodes
    stack=[]
    stack.append(startNode)
    visited[startNode]=True
    while stack:
        node=stack.pop()
        print(node)
        for i in graph[node]:
            if visited[i]==False:
                stack.append(i)
                visited[i]=True

graph=[[1,2],[0,2],[0,1,3],[2]]
DFS(0,4,graph)
