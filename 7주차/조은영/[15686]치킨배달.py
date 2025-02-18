from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken_stores = []

# 집과 치킨집의 좌표 저장
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_stores.append((r, c))

# 치킨 거리 계산 함수
def calculate_chicken_distance(selected_chickens):
    total_distance = 0
    for hr, hc in houses:
        min_distance = float('inf')
        for cr, cc in selected_chickens:
            min_distance = min(min_distance, abs(hr - cr) + abs(hc - cc))
        total_distance += min_distance
    return total_distance

# 모든 조합을 시도하여 최소 치킨 거리 찾기
min_chicken_distance = float('inf')

for selected in combinations(chicken_stores, M):
    min_chicken_distance = min(min_chicken_distance, calculate_chicken_distance(selected))

print(min_chicken_distance)
