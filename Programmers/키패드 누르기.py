'''
문제 : 키패드 누르기
링크 : https://programmers.co.kr/learn/courses/30/lessons/67256
피드백
  - 거리 구할 때 w, l 나눌 필요 없었음
  - 풀이 방법 다양함
'''

def get_distance(now, target):
    w = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    l = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    
    for i in range(len(w)):
        if now in w[i]:
            nw = i
        if target in w[i]:
            tw = i
            
    for i in range(len(l)):
        if now in l[i]:
            nl = i
        if target in l[i]:
            tl = i
            
    return abs(nw-tw) + abs(nl-tl)

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            left = n
        if n in [3,6,9]:
            answer += 'R'
            right = n
        if n in [2,5,8,0]:
            ld = get_distance(left, n)
            rd = get_distance(right, n)
            if ld < rd:
                answer += 'L'
                left = n
            elif ld > rd:
                answer += 'R'
                right = n
            elif hand == 'left':
                answer += 'L'
                left = n
            else:
                answer += 'R'
                right = n
    
    return answer