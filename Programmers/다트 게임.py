'''
문제 : 다트 게임
링크 : https://programmers.co.kr/learn/courses/30/lessons/17682
피드백 :
 - 10을 k로 치환하는 아이디어
 - 정규식 사용
'''

### 내풀이
def solution(dartResult):
    answer = [0]
    i = 0
    for j in range(len(dartResult)):
        if dartResult[j].isdigit():
            if dartResult[j] == '0' and dartResult[j-1] == '1':
                answer[i] = 10
            else:
                answer.append(int(dartResult[j]))
                i += 1
        elif dartResult[j] == 'D':
            answer[i] = answer[i] ** 2
        elif dartResult[j] == 'T':
            answer[i] = answer[i] ** 3
        elif dartResult[j] == '*':
            answer[i], answer[i-1] = answer[i] * 2, answer[i-1] * 2
        elif dartResult[j] == '#':
            answer[i] = -answer[i]

    return sum(answer)

# 다른사람풀이 ( 정규식 ) 
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 다른사람풀이 ( 10 치환 ) 
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)