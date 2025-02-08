from collections import deque
import sys

input = sys.stdin.read
def escape_fire():
    # 입력 처리
    data = input().splitlines()
    R, C = map(int, data[0].split())
    maze = [list(row) for row in data[1:R+1]]

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 불과 지훈이의 초기 위치 찾기
    fire_queue = deque()
    jihun_queue = deque()
    fire_time = [[-1] * C for _ in range(R)]  # 불의 도착 시간
    jihun_time = [[-1] * C for _ in range(R)]  # 지훈이의 도착 시간

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':  # 불의 시작 위치
                fire_queue.append((i, j))
                fire_time[i][j] = 0  # 불의 시작 시간
            elif maze[i][j] == 'J':  # 지훈이의 시작 위치
                jihun_queue.append((i, j))
                jihun_time[i][j] = 0  # 지훈이의 시작 시간

    # 🔥 불의 BFS (불이 확산되는 시간 계산)
    while fire_queue:
        x, y = fire_queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == '.' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx, ny))

    # 🏃‍♂️ 지훈이의 BFS (탈출 여부 확인)
    while jihun_queue:
        x, y = jihun_queue.popleft()
        # 가장자리 도달 시 탈출 성공
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            print(jihun_time[x][y] + 1)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == '.' and jihun_time[nx][ny] == -1:
                # 불보다 먼저 도착할 수 있어야 이동 가능
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))

    print("IMPOSSIBLE")  # 탈출 불가능한 경우

escape_fire()
