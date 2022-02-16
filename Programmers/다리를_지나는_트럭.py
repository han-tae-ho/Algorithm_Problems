'''
문제링크 : https://programmers.co.kr/learn/courses/30/lessons/42583﻿
다리를 지나는 트럭
'''

###### 첫번째 풀이 -> 테스트 5 시간초과 ########
from collections import deque
'''
브리지 길이 만틈 큐 만들고
무게 이하일때 트럭 올린다. 이동포함 1초
무게 이상일때 이동 1초
'''

def solution(bridge_length, weight, truck_weights):
    # 브릿지 길이 큐
    bridge = deque([0] * bridge_length)
    # 트럭 순서랑 무게 큐
    truck_que = deque(truck_weights)
    
    answer = 0
    while truck_que:
        if bridge[-1] != 0 :
            bridge[-1] = 0
        if sum(bridge) + truck_que[0] <= weight:
            truck = truck_que.popleft()
            bridge.rotate(1)
            bridge[0] = truck
        else:
            bridge.rotate(1)
        
        answer += 1
        print(f"{answer} 초 후 다리에는 {bridge}가 있고 트럭대기는 {truck_que}")
    
    #마지막 트럭이 실렸을 때 끝가지 가는 시간 더함
    answer += bridge_length
    return answer

############ 두번째 풀이 ############
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 브릿지 길이 큐
    bridge = deque()
    # 트럭 순서랑 무게 큐
    truck_que = deque(truck_weights)
    
    answer = 0
    while truck_que:
        answer += 1
        if len(bridge) == bridge_length:
            bridge.pop()
        if sum(bridge) + truck_que[0] <= weight:
            truck = truck_que.popleft()
            bridge.appendleft(truck)
        else:
            bridge.appendleft(0)
        
        
    
    #마지막 트럭이 실렸을 때 끝가지 가는 시간 더함
    answer += bridge_length
    return answer

############ 세번째 - class 이용 ############
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()
