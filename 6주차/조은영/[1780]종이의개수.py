import sys

input = sys.stdin.read
sys.setrecursionlimit(10**6)

# -1, 0, 1의 개수를 저장하는 변수
count = { -1: 0, 0: 0, 1: 0 }

# 종이가 같은 숫자로 이루어졌는지 확인하는 함수
def check_paper(x, y, size):
    first = paper[x][y]  # 첫 번째 값 기준
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:  # 다른 숫자가 있으면 분할
                return False
    return True

# 분할 정복 함수
def divide_and_conquer(x, y, size):
    if check_paper(x, y, size):  # 종이가 하나의 숫자로 이루어졌다면
        count[paper[x][y]] += 1  # 해당 숫자의 개수 증가
        return

    # 3x3 분할 (9등분)
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            divide_and_conquer(x + i * new_size, y + j * new_size, new_size)

# 입력 받기
data = input().split()
N = int(data[0])
paper = [list(map(int, data[i * N + 1 : (i + 1) * N + 1])) for i in range(N)]

# 분할 정복
divide_and_conquer(0, 0, N)

print(count[-1])
print(count[0])
print(count[1])
