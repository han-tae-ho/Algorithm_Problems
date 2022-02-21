'''
문제 : 주사위 굴리기
링크 : https://www.acmicpc.net/problem/14499
피드백
    - 문제 조건 꼼꼼히 !, 맵값이 주사위에 복사되면 맵값 0으로 변하는 거 구현안해서 틀렸었음
    - 확실히 하루에 한문제씩 풀다보니깐 속도도 올라가고 쉽게 푸는 것 같다.
'''


def move(d):
    global dice1, dice2, dice3
    # 동쪽이동 
    # 좌->위 위->우, 우,아래     아래가 좌
    if d == 1:
        dice2, dice1 = dice1, dice2[::-1]
    
    # 서쪽이동
    # 위->좌,   아래->우,    좌-> 아래,    우-> 위
    elif d == 2:
        dice1, dice2 = dice2, dice1[::-1]
    
    # 북쪽이동
    # 위 뒤, 아래 앞         앞 위   뒤 아래
    elif d == 3:
        dice3, dice1 = dice1, dice3[::-1]

    # 남쪽이동
    # 위 아래 -> 앞 뒤     앞 뒤 - > 아래 뒤
    else:
        dice1, dice3 = dice3, dice1[::-1]
        
dice1 = [0, 0] # 위, 아래
dice2 = [0, 0] # 좌, 우
dice3 = [0, 0] # 앞, 뒤
directions = [(0,1), (0,-1), (-1,0), (1, 0)]

N, M, sx, sy, K = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
command = list(map(int,input().split()))

def sol():
    global MAP, sx, sy
    for c in command:
        nx, ny = sx + directions[c-1][0], sy + directions[c-1][1]

        if nx >= N or ny >= M or nx < 0  or ny < 0:
            continue

        move(c)

        # 주사위값 복사 
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = dice1[1]
        else:
            dice1[1] = MAP[nx][ny]

        sx, sy = nx, ny        
        print(dice1[0])
        
if __name__ == '__main__':
    sol()