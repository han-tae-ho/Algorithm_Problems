'''
문제 : 신고 결과 받기
링크 : https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
피드백
  - list comprehension 할 때 조건문 위치 정리 (유용노트에 정리)
  - 다른사람풀이 피드백 
    - reports = {x : 0 for x in id_list}
    - answer[id_list.index(r.split()[0])] += 1
    - 인덱스 가져와서 쓰는 것 좋은 듯
'''

# 내풀이
def solution(id_list, report, k):
    #key : id, #value : 그 id가 신고한 ID list(중복빼고 담음)
    rtr_dict = dict(zip(id_list, [[] for _ in range(len(id_list))]))
    #key : id, #value : 그 id가 신고당한 횟수
    rtd_dict = dict.fromkeys(id_list, 0) 
    for r in report:
        rtr, rtd = r.split()
        if rtd not in rtr_dict[rtr]:
            rtr_dict[rtr].append(rtd)
            rtd_dict[rtd] += 1
    
    answer = []
    banned = [key for key,value in rtd_dict.items() if value >= k]
    for kk, vv in rtr_dict.items():
        ans = len(vv) - len(set(vv) - set(banned))
        answer.append(ans)
    return answer

# 다른사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer