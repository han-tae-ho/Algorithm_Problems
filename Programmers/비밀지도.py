'''
문제 : 비밀지도
링크 : https://programmers.co.kr/learn/courses/30/lessons/17681
피드백
  - 비트 연산자 사용
'''

# 내풀이
def map_sum(arr11, arr22,n):
    answer = []
    for a, b in zip(arr11, arr22):
        ans = ''
        for i in range(n):
            if a[i] == '1' or b[i] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer
            

def solution(n, arr1, arr2):
    arr11 = [bin(x)[2:].zfill(n) for x in arr1]
    arr22 = [bin(x)[2:].zfill(n) for x in arr2]
    answer = []
    return map_sum(arr11, arr22,n)

# 다른사람풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer