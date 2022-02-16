'''
문제 : 디스크 컨트롤러
링크 : https://programmers.co.kr/learn/courses/30/lessons/42627﻿
'''

### 풀이
import heapq

def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap= []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now-current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))