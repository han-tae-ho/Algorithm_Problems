'''
문제 : 크레인 인형뽑기 게임
링크 : https://programmers.co.kr/learn/courses/30/lessons/64061
피드백
  - 더 깔끔한 코드로
'''

import numpy as np
from collections import deque

def solution(board, moves):
    b = np.array(board).T.tolist()
    for doll in b:
        for i in range(len(b[0])):
            try:
                doll.remove(0)
            except:
                continue
    answer, s = 0, []
    for m in moves:
        if len(b[m-1]) >= 1:
            s.append(b[m-1][0])
            del b[m-1][0]

    before_len = len(s)
    before = ''
    while s != before:
        before = s[:]
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                del s[i]
                del s[i]
                break

    return before_len - len(s)