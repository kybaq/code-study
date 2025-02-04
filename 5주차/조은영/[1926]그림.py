import sys
from collections import deque

def bfs(x, y, n, m, graph, visited):

    # 이동 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐 선언 및 시작점 추가
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True  # 방문 처리
    area = 1  # 현재 그림의 넓이 (시작점 포함)

    while queue:
        cx, cy = queue.popleft()  # 현재 좌표 꺼내기

        # 상하좌우로 이동하며 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위 내에 있고, 아직 방문하지 않았으며, 1인 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True  # 방문 처리
                area += 1  # 넓이 증가

    return area  # 최종 넓이 반환

def solution():
    # 입력 받기
    n, m = map(int, sys.stdin.readline().split())  # 도화지 크기 입력 받기
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 도화지 정보 입력 받기

    # 방문 체크 배열
    visited = [[False] * m for _ in range(n)]

    count = 0  # 그림 개수
    max_area = 0  # 최대 그림 넓이

    # 도화지 전체 탐색
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:  # 1이면서 방문하지 않은 경우
                count += 1  # 그림 개수 증가
                max_area = max(max_area, bfs(i, j, n, m, graph, visited))  # BFS 실행 후 최대 넓이 갱신

    # 결과 출력
    print(count)  # 그림 개수
    print(max_area)  # 가장 큰 그림의 넓이

# 실행
solution()
