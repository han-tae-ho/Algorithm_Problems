'''
문제 : 2048
링크 : https://www.acmicpc.net/problem/12100﻿
'''

#### 내풀이 -> 비효율(시간초과 가능성)
from itertools import product
import copy

def up(BOARD): # x 0 -> 2 
    added = {}
    n = len(BOARD)
    for x in range(n):
        for y in range(n):
            nx, ny = x, y
            while nx - 1 >= 0 and BOARD[nx-1][y] == 0:
                nx -= 1
                # 이동
                BOARD[nx][y] = BOARD[nx+1][y]
                BOARD[nx+1][y] = 0


            if nx >= 1:
                # 값이 같을 때
                if BOARD[nx][y] == BOARD[nx-1][y]:
                    # 합치기
                    if (nx-1, y) not in added:
                        BOARD[nx-1][y] *= 2
                        added[(nx-1,y)] = 1
                        BOARD[nx][ny] = 0

    return BOARD

def down(BOARD): # x 2 -> 0 
    added = {}
    n = len(BOARD)
    for x in range(n-1,-1,-1):
        for y in range(n):
            nx, ny = x, y
            while nx + 1 < n and BOARD[nx+1][y] == 0:
                nx += 1
                # 이동
                BOARD[nx][y] = BOARD[nx-1][y]
                BOARD[nx-1][y] = 0


            if nx < n-1:
                # 값이 같을 때
                if BOARD[nx][y] == BOARD[nx+1][y]:
                    # 합치기
                    if (nx+1, y) not in added:
                        BOARD[nx+1][y] *= 2
                        added[(nx+1,y)] = 1
                        BOARD[nx][ny] = 0

    return BOARD

def left(BOARD): # x 0 -> 2 
    added = {}
    n = len(BOARD)
    for x in range(n):
        for y in range(n):
            nx, ny = x, y
            while ny - 1 >= 0 and BOARD[x][ny-1] == 0:
                ny -= 1
                # 이동
                BOARD[x][ny] = BOARD[x][ny+1]
                BOARD[x][ny+1] = 0


            if ny >= 1:
                # 값이 같을 때
                if BOARD[x][ny] == BOARD[x][ny-1]:
                    # 합치기
                    if (x, ny-1) not in added:
                        BOARD[x][ny-1] *= 2
                        added[(x, ny-1)] = 1
                        BOARD[nx][ny] = 0

    return BOARD

def right(BOARD): # y 2 -> 0 
    added = {}
    n = len(BOARD)
    for x in range(n):
        for y in range(n-1,-1,-1):
            nx, ny = x, y
            while ny + 1 < n and BOARD[x][ny+1] == 0:
                ny += 1
                # 이동
                BOARD[x][ny] = BOARD[x][ny-1]
                BOARD[x][ny-1] = 0


            if ny < n-1:
                # 값이 같을 때
                if BOARD[x][ny] == BOARD[x][ny+1]:
                    # 합치기
                    if (x, ny+1) not in added:
                        BOARD[x][ny+1] *= 2
                        added[(x,ny+1)] = 1
                        BOARD[nx][ny] = 0

    return BOARD

def solution():
    n = int(input())
    BOARD = []
    for _ in range(n):
        BOARD.append(list(map(int, input().split())))

    answer = 0
    commands = list(product(['u','d','l','r'], repeat=5))
    for com in commands:
        B = copy.deepcopy(BOARD)
        for c in com:
            if c == 'u': B = up(B)
            if c == 'd': B = down(B)
            if c == 'l': B = left(B)
            if c == 'r': B = right(B)
        max_value = max(map(max, B))
        if max_value > answer:
            answer = max_value

        del(B)

    print(answer)

solution()



#### 더 좋은 풀이
N = int(input())
original_board = [list(map(int, input().split())) for _ in range(N)]

direction = ['l', 'u', 'r', 'd']


def max_element(matrix):
    result = 0
    for rows in matrix:
        rows.append(result)
        result = max(rows)
    return result


def move_left(mat):
    result = []
    for rows in mat:
        new_row = []
        temp = 0
        for num in rows:
            if num == 0: continue
            if temp == num:
                new_row[-1] *= 2
                temp = 0
            else:
                new_row.append(num)
                temp = num
        new_row += [0] * (len(rows) - len(new_row))
        result.append(new_row)

    return result


def move_up(mat):
    result = move_left(list(map(list, zip(*mat))))
    return list(map(list, zip(*result)))


def move_right(mat):
    result = []
    result = []
    for rows in mat:
        rows.reverse()
        new_row = []
        temp = 0
        for num in rows:
            if num == 0: continue
            if temp == num:
                new_row[-1] *= 2
                temp = 0
            else:
                new_row.append(num)
                temp = num
        new_row += [0] * (len(rows) - len(new_row))
        new_row.reverse()
        result.append(new_row)
    return result


def move_down(mat):
    result = move_right(list(map(list, zip(*mat))))
    return list(map(list, zip(*result)))


def dfs(board, n):
    global answer
    if n == 5:
        answer = max(answer, max_element(board))
        return

    else:
        dfs(move_left(board), n+1)
        dfs(move_right(board), n+1)
        dfs(move_up(board), n+1)
        dfs(move_down(board), n+1)


answer = 0
dfs(original_board, 0)
print(answer)


#### 피드백
'''
● 시간 제한이 있었으면 내 풀이로는 해결을 못한다.
    - 최대 5번 이동 시 이기 때문에 product 사용해서 1024 가지 계산해도 괜찮을거라고 생각했다.
    - dfs 재귀함수로 이용하여 풀자
    
● original_graph 가져와서 함수 계산 할 때 deepcopy 사용!
    - 2차원 이상 리스트면 얕은 복사로 불가능. 1차원이면 list[:] 로 해도 문제없다.
    
● move 함수 구현 시 up, left 와 down, right 는 input graph를 transpose 형태로 하면 간단히 구현 가능
    - zip과 map 이용
    - np T 이용
    
● move 함수 구현 시에 인덱스 문제( 경계 넘어가는 경우 ) 를 try, except 로 구현하면 가독성 증가

● answer 구할때 조건문 사용 말고 max(a, b) 사용하는 것도 생각하기
    - 너무 max(list) 만 생각하는 것 같다.
    
● dfs 재귀함수 구현 기본부터 응용 많이 이해하고 생각하기
'''