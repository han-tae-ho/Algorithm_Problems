'''
문제 : 가장 먼 노드
링크 : https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3 
'''

### 내풀이
from collections import deque

def solution(n, vertex):
    l = len(vertex)
    graph = [[] for i in range(l+1)]
    for (s, e) in vertex:
        graph[s].append(e)
        graph[e].append(s)
        
    distances = [-1] * ( n + 1 )
    q = deque([1])
    distances[1] = 0 
    
    while q:
        now = q.popleft()     
        for node in graph[now]:
            if distances[node] == -1:
                q.append(node)
                distances[node] = distances[now]+1
                
    return distances.count(max(distances))