import sys

input = sys.stdin.read
data = input().split("\n")

# N값 읽기
N = int(data[0].strip())

# 색종이 행렬
paper = [list(map(int, data[i + 1].split())) for i in range(N)]

# 색종이 개수 저장 변수
white = 0  # 0의 개수
blue = 0   # 1의 개수

# 분할 정복 함수
def divide_and_conquer(x, y, size):
    global white, blue

    # 첫 번째 원소를 기준으로 모든 원소가 같은지 확인
    first_color = paper[x][y]
    is_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first_color:
                is_same = False
                break
        if not is_same:
            break

    # 모두 같은 색이라면 해당 색 카운트 증가
    if is_same:
        if first_color == 0:
            white += 1
        else:
            blue += 1
        return

    # 다른 색이 포함된 경우 4등분하여 재귀 호출
    half = size // 2
    divide_and_conquer(x, y, half)                # 왼쪽 위
    divide_and_conquer(x, y + half, half)         # 오른쪽 위
    divide_and_conquer(x + half, y, half)         # 왼쪽 아래
    divide_and_conquer(x + half, y + half, half)  # 오른쪽 아래

# 분할 정복 실행
divide_and_conquer(0, 0, N)

print(white)
print(blue)
