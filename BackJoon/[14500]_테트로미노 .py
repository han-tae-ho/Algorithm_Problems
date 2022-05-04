from itertools import product

def poliomino(x, y):
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    pol = []
    for commands in list(product(moves, repeat = 3)):
        p = [(x, y)]
        sx, sy = x, y
        v = [(x, y)]
        for com in commands:
            nx, ny = sx + com[0], sy + com[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or (nx, ny) in v:
                break
            v.append((nx, ny))
            p.append((nx, ny))
            sx, sy = nx, ny
        if len(p) == 4:
            pol.append(p)

    return pol

def get_max_position():
    max_value = max(map(max, MAP))
    positions = []
    for r in range(n):
        for c in range(m):
            if MAP[r][c] == max_value:
                positions.append((r,c))
    return positions

def get_value(a):
    x, y = a[0], a[1]
    return MAP[x][y]

def sol():
    ans = 0
    for (x, y) in get_max_position():
        pols = poliomino(x, y)
        for pol in pols:
            s = sum(list(map(get_value, pol)))
            ans = max(ans, s)   
    print(ans)
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    sol()