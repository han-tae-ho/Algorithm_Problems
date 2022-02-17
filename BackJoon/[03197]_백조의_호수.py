'''
문제 : 백조의 호수
링크 : https://www.acmicpc.net/problem/3197
피드백
- python3 -> pypy3
   - PyPy3에서는 실행시, 자주 쓰이는 코드를 캐싱하는 기능
   - 즉 메모리를 조금 더 사용하여 그것들을 저장하고 있어, 실행속도를 개선 가능
   - 간단한 코드상에서는 Python3, 복잡한 코드(반복)을 사용하는 경우 PyPy3
    
- 로컬 변수와 전역 변수 개념 다시 잡기.
   - 로컬에서 전역변수에 값 할당 할 경우 global 사용
   - ex) 전역변수가 a 일때 로컬 함수에서 print(a) 등은 가능하지만 a = 2 로 할당하는 경우 오류
    
- 문제에서 얼음이 녹을때 마다 백조가 만날 수 있는지 확인하는 코드에서 확인할때 
그 때 맵 상태에서 새로 확인하는 것은 시간이 오래걸림
   - 이전 맵에서 얼음이 녹은 부분만 방문처리하면 되기때문에 이전 맵 visited 를 가져와서 그대로 사용 -> 시간 단축
   - 첫 코드 시간초과 이유
'''


### 첫 풀이 -> 시간 초과
import sys
from collections import deque
# input = sys.stdin.readline
n, m = map(int, input().split())

MAP = [list(input().strip()) for _ in range(n)]

p = []
for r in range(n):
    for c in range(m):
        if MAP[r][c] == 'L':
            p.append(r)
            p.append(c)

sx, sy, ex, ey = p  # 백조 2마리 위치      

def is_meet():
    q = deque([(sx, sy)])
    visited = [(sx, sy)]
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:            
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or MAP[nx][ny] == 'X':
                continue
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                q.append((nx, ny))
            if nx == ex and ny == ey:
                return True
    return False


def melt():
    global MAP
    visited = []
    melted = []
    for r in range(n):
        for c in range(m):
            if MAP[r][c] == '.' and (r, c) not in visited:
                visited = [(r, c)]
                q = deque([(r, c)])
            while q:
                x, y = q.popleft()
                for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:            
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or (nx, ny) in visited:
                        continue
                    else:
                        if (MAP[nx][ny] == 'X'):
                            if (nx, ny) not in melted:
                                melted.append((nx, ny))

                        else:
                            visited.append((nx, ny))
                            q.append((nx, ny))
    for x, y in melted:
        MAP[x][y] = '.'

ans = 0
while True:
    if is_meet():
        break
    melt()
    ans += 1

print(ans)

### 최종코드
from collections import deque
from sys import stdin
input = stdin.readline

ex, ey, ans = 0, 0, 0
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
R, C = map(int, input().split())
a = [list(input().strip()) for _ in range(R)]
wc = [[False]*C for _ in range(R)]
sc = [[False]*C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

def water():
    while wq1:
        x, y = wq1.popleft()
        a[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            wc[nx][ny] = True

def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = True
    return False

for i in range(R):
    for j in range(C):
        if a[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = True
            else:
                ex, ey = i, j
            a[i][j] = '.'
        if a[i][j] == '.':
            wq1.append((i, j))
            wc[i][j] = True
while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1
print(ans)