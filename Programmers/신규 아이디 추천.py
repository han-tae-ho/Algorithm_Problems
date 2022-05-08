'''
문제 : 신규아이디추천
링크 : https://programmers.co.kr/learn/courses/30/lessons/72410
피드백
  - 정규식 표현 블로그 정리
'''

import re

def solution(new_id):
    s = new_id[:]
    # 1
    s = s.lower()
    # 2
    s = re.sub("[^a-z0-9-_.]","",s)
    # 3
    s = re.sub("\.+",".",s)
    # 4
    s = re.sub("^\.|\.$","",s)
    # 5
    if s == "": s = "a"
    # 6-1
    if len(s) >= 16: s = s[:15]
    # 6-2
    s = re.sub("\.$","",s)
    # 7
    while len(s) < 3: s = s + s[-1]
    
    return s