# 2606 바이러스 
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,visited):
    visited[v] = True   # 방문 여부..
    for num in graph[v]:
        if not visited[num]:
            dfs(num, visited)

visited = [False] * (n+1)
dfs(1, visited)

print(visited.count(True)-1)