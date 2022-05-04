'''
문제 : 연구소
링크 : https://www.acmicpc.net/problem/14502
피드백
    - virus bfs 돌릴 때 큐에 한 번에 넣고 하면 되는데 왜 하나씩 했을까??
    - 벽을 세우는 알고리즘.. 완전 탐색말고 경웨 따라 효율적으로 하는 방법 생각 -> 시간 줄이기
'''

from collections import deque
import copy
from itertools import combinations
import sys
input = sys.stdin.readline

def bfs():
    global graph
    global answer
    '''
    start (x, y)
    '''
    v = []
    q = deque([])
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                v.append([i,j])
                q.append([i,j])

    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >=n or ny >= m or graph[nx][ny] == 1 or (nx,ny) in v:
                continue
            else:
                q.append((nx,ny))
                graph[nx][ny] = 2
                v.append((nx,ny))
                
    cnt = 0
    for i in graph:
        cnt+=i.count(0)
    answer = max(answer,cnt)

n, m = map(int, input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(int, input().split())))
    
zeros = []
for nn in range(n):
    for mm in range(m):
        if MAP[nn][mm] == 0:
            zeros.append((nn,mm))
                    
answer = 0
for (aa,bb),(cc,dd),(ee,ff) in list(combinations(zeros,3)):
    graph = copy.deepcopy(MAP)
    graph[aa][bb] = 1
    graph[cc][dd] = 1
    graph[ee][ff] = 1
    
    bfs()
    
print(answer)
    
    
