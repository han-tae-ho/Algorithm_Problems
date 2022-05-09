'''
문제 : 실패율
링크 : https://programmers.co.kr/learn/courses/30/lessons/42889
피드백
  - 다른 사람 풀이가 시간 상 더 빠름
'''

def solution(N, stages):
    stages = np.array(stages)
    d = {}
    for i in range(1,N+1):
        stages = stages[np.where(stages >= i)] 
        try_num = len(stages)
        success = sum(np.where(stages == i,1,0))
        try:
            d[i] = success / try_num
        except:
            d[i] = 0
        
    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return list(d.keys())

# 다른 사람 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)