import sys

N = int(sys.stdin.readline().strip())  # 집 개수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 비용 리스트

# DP 배열 초기화 (첫 번째 집은 그대로 사용)
dp = [[0] * 3 for _ in range(N)]
dp[0] = cost[0]  # 첫 번째 집의 비용 그대로 사용

# DP 테이블 채우기
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # 빨강
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # 초록
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # 파랑

# 최소 비용 출력
print(min(dp[N-1]))  # 마지막 집에서 최소 비용 선택
