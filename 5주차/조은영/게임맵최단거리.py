from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 행, 열 크기
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 이동
    queue = deque([(0, 0, 1)])  # (현재 위치 x, 현재 위치 y, 이동 거리)
    
    while queue:
        x, y, dist = queue.popleft() # 현재 위치에서 이동 거리 꺼내기
        
        # 목표 지점에 도착하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            
            # 맵 범위 안에 있고, 이동 가능한 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문 처리 (다시 방문하지 않도록)
                queue.append((nx, ny, dist + 1))  # 거리 증가
    
    return -1  # 상대 팀 진영에 도달할 수 없는 경우
