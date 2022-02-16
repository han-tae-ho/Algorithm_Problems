'''
문제 : 평범한 배낭
링크 : https://www.acmicpc.net/problem/12865﻿
피드백
    ● knapsack 알고리즘. 이해하기 쉽기 위해 2차원 리스트로 구현 했지만 1차원 리스트로도 가능. (이전 row만 보면 되므로)
    ● 리스트뿐만 아니라 사전으로도 구현 (다른 사람 풀이)
    ● 2차원 배열 생성할 때 "[[0] * n] * m]" 으로 구현 X. 인덱스 할당시 모든 col 값 변함(포인터).
        - "[[0] * n for _ in range(m)]" 사용
    ● 바다코끼리 연산자 <the walrus operator> := 이해
    ● 사전 get / update 적용 생각하기
    ● 문제 기준을 확실하게 하기. 다른사람 풀이에서 items 순서를 vv, ww 로 한 이유 알기
'''

#### 내풀이
N, K = map(int, input().split())
items = [list(map(int,input().split())) for _ in range(N)]
L = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = items[i-1]
        if w > j:
            L[i][j] = L[i-1][j]
        else:
            L[i][j] = max(L[i-1][j], L[i-1][j-w] + v)
print(L[N][K])


#### 다른사람 풀이
import sys
input=sys.stdin.readline
def sol():
    n,k=map(int,input().split())
    kk=k+1
    bag=dict()
    bag[0]=0
    data=[tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)
    for w,v in data:
        tmp={}
        for vv,ww in bag.items():
            if bag.get(vvv:=vv+v,kk)>(www:=w+ww):
                tmp[vvv]=www
        bag.update(tmp)
    print(max(bag.keys()))
sol()