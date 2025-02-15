#문제 이해
# N x N 체스판 위에 N개의 퀸을 서로 공격할 수 없도록 배치하는 경우의 수를 찾는 문제
# 퀸은 같은 행, 같은 열, 대각선 방향으로 공격할 수 있으므로 퀸을 배치할 때는 이 조건들을 체크해야함

#예제 이해
# 입력: 8
# 출력: 92
# 8x8 체스판에서 퀸 8개를 놓을 수 있는 경우의 수는 92가지

#아이디어 창출
# 1) 백트래킹을 활용하여 퀸을 한 줄씩 배치
# 2) 같은 열, 같은 대각선 방향을 체크하여 놓을 수 있는지 확인
# 3) 퀸을 배치하면 다음 행으로 이동하여 재귀적으로 탐색
# 4) N개의 퀸을 배치하면 경우의 수를 증가시키고, 이전 상태로 돌아감

#아이디어를 문제에 적용
# 1) `N`을 입력받음
# 2) 한 줄씩 퀸을 배치하면서 조건을 만족하는지 체크
# 3) `cols`, `diag1`, `diag2` 리스트를 활용하여 빠르게 유효성 검사
# 4) 퀸을 배치할 수 있다면 다음 행으로 이동하고, 모든 행을 채우면 경우의 수 증가
# 5) 백트래킹으로 퀸을 제거하고 다른 경우를 탐색하며 원상 복구


import sys
input = sys.stdin.read

# 백트래킹을 위한 함수
def place_queens(row):
    global count
    if row == N:  # 모든 퀸을 배치했다면 경우의 수 증가
        count += 1
        return
    
    for col in range(N):
        if not cols[col] and not diag1[row - col] and not diag2[row + col]:
            # 퀸 배치
            cols[col] = diag1[row - col] = diag2[row + col] = True
            place_queens(row + 1)  # 다음 행으로 이동
            # 백트래킹 (원상 복구)
            cols[col] = diag1[row - col] = diag2[row + col] = False

# 입력 받기
N = int(input().strip())
count = 0
cols = [False] * N  # 열 방문 여부
diag1 = [False] * (2 * N)  # / 대각선 방문 여부
diag2 = [False] * (2 * N)  # \ 대각선 방문 여부

# 백트래킹 실행
place_queens(0)

print(count)