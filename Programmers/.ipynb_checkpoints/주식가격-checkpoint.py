'''
문제 : 주식가격
링크 : https://programmers.co.kr/learn/courses/30/lessons/42584﻿
'''

##### 첫풀이
from collections import deque
import copy

def solution(prices):    
    answer = []
    q = deque(prices)
    
    count = 0
    while q:
        num = q.popleft()
        rest_q = copy.deepcopy(q)
        
        while rest_q:
            count += 1
            if num > rest_q.popleft():
                break
            
        answer.append(count)
        count=0
            
    return answer

##### 두번째풀이 - 효율성 up (deepcopy 사용 x)
from collections import deque
import copy

def find_index(num, q):
    for i, _ in enumerate(q):
        if _ < num:
            return i+1
    return len(q)
        

def solution(prices):    
    answer = []
    q = deque()
    for _ in prices:
        q.append(_)
    
    while q:
        num = q.popleft()
        answer.append(find_index(num, q))
            
    return answer