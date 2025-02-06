from collections import deque

def bfs(maze, N, M):
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 (시작 위치: (0, 0), 거리: 1)
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, dist = queue.popleft()  # 현재 위치와 거리 가져오기
        
        # 도착 지점에 도달하면 거리 반환
        if x == N - 1 and y == M - 1:
            return dist
        
        # 상, 하, 좌, 우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 새로운 좌표 계산
            
            # 맵 범위 내에 있고, 이동 가능하면 큐에 추가
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny, dist + 1))  # 거리 +1 후 추가

    return -1  # 도달할 수 없는 경우 (항상 도달 가능하므로 필요 없음)

# 입력 처리
N, M = map(int, input().split())  # 행, 열 크기 입력
maze = [list(map(int, list(input().strip()))) for _ in range(N)]  # 미로 입력

# 최소 칸 수 출력
print(bfs(maze, N, M))
