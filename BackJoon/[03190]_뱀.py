'''
문제 : 뱀
링크 : https://www.acmicpc.net/problem/3190
피드백
    - 쉽게 풀어서 없뜸 !
'''


import sys
from collections import deque
# input = sys.stdin.readline
N = int(input()) # 맵크기 n*n
K = int(input())
apple = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
moves = {}
for i in range(L):
    X, C = input().split()
    moves[int(X)] = C

dir_ = [(0, 1), (1, 0), (0, -1), (-1, 0)] ## 우, 하, 좌, 상
MAP = [[0] * N for _ in range(N)]
for r, c in apple:
    MAP[r-1][c-1] = 'a'

def sol():
    global MAP
    d = 0
    time = 0
    body = deque([(0, 0)])
    nx, ny = 0, 0
    while True:
        nx = nx + dir_[d][0]
        ny = ny + dir_[d][1]
        time += 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx, ny) in body:
            return time
        if MAP[nx][ny] == 'a':
            MAP[nx][ny] = 0
        else:
            body.popleft()
        body.append((nx, ny))

        if time in moves.keys():
            if moves[time] == 'L':
                d = (d - 1)
            else:
                d = (d + 1)
            if d >= 4:
                d -= 4
            if d < 0 :
                d += 4

print(sol())