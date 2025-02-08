#문제 이해
# 창고에 보관된 토마토가 익는 최소 일수를 구하는 문제
# 목표:
# 	1) 모든 토마토가 익는데 걸리는 최소 일수를 출력.
# 	2) 모두 처음부터 익어있으면 => 0
# 	3) 모두 익지 못하는 경우 => -1 출력

# 예제 이해

# 예제 1
# 입력:
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 	1) 맨 아래 오른쪽의 1이 익어 있는 토마토
# 	2) BFS를 통해 하루에 한 칸씩 익어감
# 결과: 8일 후 모든 토마토가 익음

# 예제 2
# 입력:
# 6 4
# 0 -1 0 0 0 0
# -1 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
#  1) -1(빈 공간) 때문에 익을 수 없는 토마토가 발생.
# 결과: -1 출력
 
#아이디어 추출
# BFS(너비 우선 탐색) 활용: 
# 	1)	초기 상태에서 모든 익은 토마토(1)를 큐에 삽입
# 	2)	BFS 탐색을 통해 상하좌우로 익음 (O(N * M))
# 	3)	마지막에 모든 0이 1이 되었는지 확인
# 	4)	남은 0이 있으면 -1 반환, 모두 익었으면 최대 일수 반환

#아이디어를 문제에 적용
# 초기 상태 저장:
#   1) grid(2차원 리스트)에 입력된 토마토 상태 저장
#   2) 익은 토마토(1) 위치를 큐에 삽입하여 동시에 익기 시작하도록 함
#   3) 익지 않은 토마토(0) 개수를 카운트하여 BFS 종료 후 익지 못한 토마토가 있는지 확인
# BFS 탐색 (토마토 익히기)
#   1) deque를 사용하여 BFS(너비 우선 탐색) 수행
# 	2) 익은 토마토가 상하좌우(4방향) 로 퍼지면서 익히기
# 	3) 새롭게 익은 토마토를 큐에 추가하고, 최소 일수를 갱신
# 최종 결과 확인
# 	1) 남아있는 0이 있다면 -1 출력 (모든 토마토가 익지 못한 경우)
# 	2) 그렇지 않다면 days를 출력 (모든 토마토가 익는데 걸린 일수)

from collections import deque
import sys

def min_days_to_ripen(grid, m, n):

    queue = deque()
    unripe = 0  # 익지 않은 토마토 개수
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동
    days = 0  # 최소 일수

    # 초기 설정 (익은 토마토 위치 큐에 추가 & 익지 않은 토마토 개수 카운트)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j, 0))  # (행, 열, 현재까지의 일수)
            elif grid[i][j] == 0:
                unripe += 1  # 익지 않은 토마토 개수 증가

    # BFS 탐색
    while queue:
        x, y, days = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 익은 토마토로 변경
                unripe -= 1  # 익지 않은 토마토 개수 감소
                queue.append((nx, ny, days + 1))  # 새롭게 익은 토마토 추가

    # 결과 반환
    return days if unripe == 0 else -1  # 익지 않은 토마토가 남아있으면 -1

# 입력 처리 및 실행
m, n = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(min_days_to_ripen(grid, m, n))