import sys
from copy import deepcopy

input = sys.stdin.read

# CCTV 감시 방향 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 종류별 감시 방향
directions = [
    [],  # 0번 인덱스는 사용 X
    [[0], [1], [2], [3]],  # 1번 CCTV (한 방향)
    [[0, 2], [1, 3]],  # 2번 CCTV (서로 반대 방향)
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번 CCTV (직각 방향)
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번 CCTV (세 방향)
    [[0, 1, 2, 3]]  # 5번 CCTV (네 방향)
]

def watch(grid, x, y, direction):
    """ 특정 방향으로 감시 영역을 표시 """
    N, M = len(grid), len(grid[0])
    nx, ny = x, y
    while True:
        nx += dx[direction]
        ny += dy[direction]
        if not (0 <= nx < N and 0 <= ny < M) or grid[nx][ny] == 6:
            break
        if grid[nx][ny] == 0:
            grid[nx][ny] = '#'

def dfs(depth, grid):
    """ 백트래킹을 이용한 CCTV 방향 조합 탐색 """
    global min_blind_spots
    
    if depth == len(cctvs):
        # 사각지대 계산
        blind_spots = sum(row.count(0) for row in grid)
        min_blind_spots = min(min_blind_spots, blind_spots)
        return
    
    x, y, type_ = cctvs[depth]
    
    for direction_set in directions[type_]:
        new_grid = deepcopy(grid)
        for direction in direction_set:
            watch(new_grid, x, y, direction)
        dfs(depth + 1, new_grid)

# 입력 처리
data = input().splitlines()
N, M = map(int, data[0].split())
grid = [list(map(int, line.split())) for line in data[1:N+1]]

# CCTV 정보 저장
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= grid[i][j] <= 5:
            cctvs.append((i, j, grid[i][j]))

# 최소 사각지대 초기값 설정
min_blind_spots = float('inf')

dfs(0, grid)

print(min_blind_spots)
