'''
문제 : 숫자 문자열과 영단어
링크 : https://programmers.co.kr/learn/courses/30/lessons/81301
피드백
  - 없음
'''

import re
def solution(s):
    l = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i, k in enumerate(l): s = re.sub(k, str(i), s)
    return int(s)