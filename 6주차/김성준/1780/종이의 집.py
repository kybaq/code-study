#문제 이해
# N x N 크기의 행렬이 주어지며, 각 칸에는 -1, 0, 1 중 하나가 들어있음
# 만약 전체 종이가 하나의 숫자로만 이루어져 있다면 그대로 사용
# 그렇지 않다면 같은 크기의 9개의 종이로 나누고 같은 과정을 반복
# 최종적으로 -1, 0, 1로만 이루어진 종이의 개수를 출력해야 함

#예제 이해
# 예제 입력을 보면 9x9 행렬이 주어짐
# 이 행렬을 확인했을 때, 한 번의 분할로 동일한 숫자로 이루어진 부분이 아니라면 9개의 작은 종이로 다시 나눠야 함
# 최종적으로 각각의 숫자(-1, 0, 1)로만 이루어진 종이의 개수를 출력해야 함

#아이디어 창출
# 1) 주어진 행렬이 하나의 숫자로만 이루어져 있는지 확인하는 함수 필요
# 2) 같은 숫자로 이루어져 있지 않다면 9개의 작은 종이로 나누고, 각각을 다시 검사
# 3) 재귀적으로 수행하면서, -1, 0, 1로만 이루어진 종이의 개수를 카운팅
# 4) 기저 조건: 종이가 하나의 숫자로만 이루어져 있다면 개수를 증가시키고 종료
# 5) 재귀 호출: 9등분하여 각각 검사

#아이디어를 문제에 적용
# 1) 입력을 받아 행렬을 2차원 리스트로 저장
# 2) 전체 행렬을 검사하여 하나의 숫자로 이루어져 있다면 해당 숫자의 개수를 증가
# 3) 만약 그렇지 않다면 N을 3등분하여 9개의 부분으로 나누고 재귀적으로 처리
# 4) 최종적으로 -1, 0, 1 각각의 개수를 출력

def count_numbers(x, y, size):
    # 현재 영역의 첫 번째 값을 저장
    number = paper[x][y]
    
    # 현재 영역이 하나의 숫자로만 이루어져 있는지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            # 만약 다른 숫자가 있다면 9등분하여 재귀적으로 검사
            if paper[i][j] != number:
                new_size = size // 3  # 종이를 3등분한 크기 계산
                for dx in range(3):
                    for dy in range(3):
                        # 9개의 작은 종이에 대해 재귀 호출
                        count_numbers(x + dx * new_size, y + dy * new_size, new_size)
                return  # 나누었으므로 더 이상 진행하지 않고 종료
    
    # 하나의 숫자로만 이루어졌다면 해당 숫자의 개수를 증가시킴
    result[number + 1] += 1

# 입력 받기 (N: 종이의 크기)
N = int(input())
# N x N 크기의 종이 데이터 입력 받기
paper = [list(map(int, input().split())) for _ in range(N)]

# -1, 0, 1의 개수를 저장할 리스트 (인덱스 0: -1 개수, 1: 0 개수, 2: 1 개수)
result = [0, 0, 0]

# 재귀 함수 실행: 종이 전체(0,0)부터 시작
count_numbers(0, 0, N)

print(result[0])  # -1로만 이루어진 종이 개수 출력
print(result[1])  # 0으로만 이루어진 종이 개수 출력
print(result[2])  # 1로만 이루어진 종이 개수 출력
