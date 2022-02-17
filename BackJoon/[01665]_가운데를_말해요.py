'''
문제 : 가운데를 말해요
링크 : https://www.acmicpc.net/problem/1655
피드백
    - maxheap 과 minheap 동시 사용하는 아이디어 (python heapq는 기본 최소힙 -> 최대힙 (-n,n))
    - 중간값 기준 양 쪽 크기 조절하며 push. 이후 minheap, maxheap. root 비교 후 swap push.
'''

### 첫풀이 -> 시간초과
from collections import deque
import sys
# input = sys.stdin.readline

n = int(input())
nums = deque([int(input()) for _ in range(n)])
sorted_nums = sorted(nums)

length = len(sorted_nums)
answers = []
while nums:
    if int(length / 2) == 0:
        i1 = int(length / 2)
        i2 = i1 - 1
        answers.append(min(sorted_nums[i1], sorted_nums[i2]))

    else:
        i = int(length / 2 - 0.5)
        answers.append(sorted_nums[i])

    now = nums.pop()
    sorted_nums.remove(now)
    length -= 1

for a in answers:
    print(a)
    
    
### 최종풀이
import heapq
import sys
# input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
left_q, right_q = [], []

for n in nums:
    if len(left_q) == len(right_q):
        heapq.heappush(left_q, (-n, n))
    else:
        heapq.heappush(right_q, (n, n))

    if right_q and left_q[0][1] > right_q[0][1]:
        a, b = heapq.heappop(left_q)[1], heapq.heappop(right_q)[1]
        heapq.heappush(left_q, (-b, b))
        heapq.heappush(right_q, (a, a))

    print(left_q[0][1])