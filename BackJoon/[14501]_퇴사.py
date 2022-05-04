'''
문제 : 퇴사
링크 : https://www.acmicpc.net/problem/14501
피드백
    - 다이나믹 프로그래밍 점화기 세우는 능력 향상시키기
    - 문제에 따라 뒤에서 할 지 앞부터 할 지 생각잘하기
    - 점화식 한 구간을 노트에 쓰면서 하면 식 세우기 편한 것 같다.
'''

def sol():
    n = int(input())
    t, p = [0],[0]
    for i in range(n):
        tt, pp = map(int, input().split())
        t.append(tt)
        p.append(pp)

    dp = [0] * (n+2)
    for day in range(n,0,-1):
        if day + t[day] > n+1:
            dp[day] = dp[day + 1]
        else:
            dp[day] = max(p[day] + dp[day + t[day]], dp[day+1])

    print(dp[1])
    
if __name__ == "__main__":
    sol()
    
    
