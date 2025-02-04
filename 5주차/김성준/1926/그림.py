#문제 이해
# 목표:
# 1) 2차원 도화지에서 1로 연결된 영역(그림)의 개수를 찾고, 가장 넓은 그림의 넓이를 구하기
# 2) 가로, 세로로 연결된 1만 같은 그림으로 간주하며, 대각선은 연결되지 않음
 
#예제 이해
# 입력
# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1
#1이 연결된 부분을 찾고, 각각의 크기를 계산

# 그림 개수 및 크기 분석
# 1️) (0,0)~(1,1) → 크기: 4
# 2️) (0,3)~(0,4) → 크기: 2
# 3️) (3,0) → 크기: 1
# 4️) (3,2)~(5,4) → 크기: 9

# 출력
# 4
# 9

#아이디어 추출

# BFS (너비 우선 탐색) 활용: 
# 	1) 2차원 배열에서 1로 연결된 영역을 탐색
# 	2) 방문한 곳은 다시 방문하지 않도록 처리
# 	3) BFS를 사용해 한 그림의 크기를 계산
# 그림 탐색 과정: 
#   1) 모든 좌표를 돌면서 1을 만나면 새로운 그림 시작
# 	2) BFS를 이용해 해당 그림의 넓이를 구하고, 방문한 곳은 0으로 변경
# 	3) 그림 개수를 증가시키고, 가장 큰 그림 크기를 갱신
 
#아이디어를 문제에 적용

# 그래프 탐색을 위한 BFS 활용
#   1) 큐(queue) 를 사용하여 연결된 1의 개수를 세는 BFS 알고리즘 적용
# 	2) 방문한 곳은 0으로 바꿔 중복 탐색 방지

# 2차원 배열을 순회하며 그림 탐색
#   1) (i, j) 위치가 1이면 BFS 시작
# 	2) 큐를 사용해 가로/세로로 연결된 1을 모두 탐색

# 탐색 종료 후 결과 출력
#   1) 총 그림 개수 출력
# 	2) 최대 그림 크기 출력
 
import sys
from collections import deque

# 입력 처리
n, m = map(int, sys.stdin.readline().split())  # 세로, 가로 크기
canvas = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 도화지 정보

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])  # BFS를 위한 큐 초기화
    canvas[x][y] = 0  # 방문 처리 (0으로 변경)
    area = 1  # 그림 크기 초기화
    
    while queue:
        cx, cy = queue.popleft()  # 현재 위치
        
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and canvas[nx][ny] == 1:  # 유효한 범위 & 미방문 1
                queue.append((nx, ny))
                canvas[nx][ny] = 0  # 방문 처리
                area += 1  # 그림 크기 증가

    return area  # 해당 그림의 크기 반환

# 그림 개수 및 최대 크기 찾기
count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1:  # 새로운 그림 발견
            count += 1
            max_area = max(max_area, bfs(i, j))  # BFS 실행 후 최대 크기 갱신

# 결과 출력
print(count)  # 총 그림 개수
print(max_area)  # 가장 넓은 그림 크기