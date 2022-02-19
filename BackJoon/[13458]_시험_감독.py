'''
문제 : 시험 감독
링크 : https://www.acmicpc.net/problem/13458
피드백
    - 내가 알아보기 쉬운 코드 대로 짰지만 다른 사람 풀이 숏코딩 보면 뭔가 더 pythonic 하게 푼 것 같다.
    - 0 보다 작은 조건 일때 0으로 만드는 것에서 min 함수를 사용하면 더 깔끔한 것 같다.
    - eval('수식' * 3) 함수 쓸 때 * 3 으로도 이용 가능
'''

### 첫풀이 (백준은 numpy 이용 불가 ) 
import numpy as np

def sol():
    A = int(input()) # 시험장 수
    students = list(map(int,(input().split()))) # 시험장 별 학생 수
    supervisers, sub_supervisers = map(int,(input().split()))
    strudents_arr = np.array(students)
    strudents_arr -= supervisers
    strudents_arr[strudents_arr < 0] = 0
    not_rest = [True if ( x % sub_supervisers != 0 and x != 0 ) else False for x in strudents_arr]
    strudents_arr = strudents_arr // sub_supervisers

    return int(len(strudents_arr) + sum(strudents_arr) + sum(not_rest))

print(sol())


### 최종코드 ( numpy 없이 구현 )
def sol():
    A = int(input()) # 시험장 수
    students = list(map(int,(input().split()))) # 시험장 별 학생 수
    supervisers, sub_supervisers = map(int,(input().split()))
    students = [x - supervisers if (x - supervisers) >= 0 else 0 for x in students]
    not_rest = [True if ( x % sub_supervisers != 0 and x != 0 ) else False for x in students]
    strudents = [x // sub_supervisers for x in students]

    return int(len(strudents) + sum(strudents) + sum(not_rest))

print(sol())

 
### 다른 사람 풀이 (ID : sait2000)
_,a,[b,c]=eval('map(int,input().split()),'*3)
print(sum(1-min(0,(b-n)//c)for n in a))