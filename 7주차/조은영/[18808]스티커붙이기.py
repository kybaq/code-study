import sys

input = sys.stdin.read
data = input().split("\n")

idx = 0
N, M, K = map(int, data[idx].split())
idx += 1

# 노트북 격자
laptop = [[0] * M for _ in range(N)]

# 스티커 회전 함수
def rotate(sticker):
    R, C = len(sticker), len(sticker[0])
    new_sticker = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            new_sticker[c][R - 1 - r] = sticker[r][c]
    return new_sticker

# 스티커 붙이는 함수
def can_attach(sticker, x, y):
    R, C = len(sticker), len(sticker[0])
    if x + R > N or y + C > M:
        return False
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1 and laptop[x + i][y + j] == 1:
                return False
    return True

def attach(sticker, x, y):
    R, C = len(sticker), len(sticker[0])
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                laptop[x + i][y + j] = 1

# 스티커 붙이기 로직
for _ in range(K):
    R, C = map(int, data[idx].split())
    idx += 1
    sticker = [list(map(int, data[idx + i].split())) for i in range(R)]
    idx += R

    # 스티커를 최대 4번 회전하면서 붙이기 시도
    placed = False
    for _ in range(4):
        for x in range(N):
            for y in range(M):
                if can_attach(sticker, x, y):
                    attach(sticker, x, y)
                    placed = True
                    break
            if placed:
                break
        if placed:
            break
        sticker = rotate(sticker)  # 회전

# 최종 스티커 개수 계산
result = sum(sum(row) for row in laptop)
print(result)
