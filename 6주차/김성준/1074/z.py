#문제 이해
# 	1) 크기가 2^N \times 2^N인 배열을 Z 모양으로 탐색하는 문제
# 	2) 배열을 4등분하여 재귀적으로 방문
# 	3) 특정 위치  (r, c) 가 몇 번째 방문인지 출력
 
#예제 이해

# 예제 1:  N = 2, r = 3, c = 1 
#   1)  2^2 \times 2^2 = 4 \times 4  배열을 다음 순서로 방문
 
# 0   1   4   5  
# 2   3   6   7  
# 8   9   12  13  
# 10  11  14  15  

# 위치  (3,1) 은 11번째 방문
 
# 예제 2:  N = 3, r = 7, c = 7 
#   1) 2^3 \times 2^3 = 8 \times 8  배열을 다음 순서로 방문
 
# 0   1   4   5   16  17  20  21  
# 2   3   6   7   18  19  22  23  
# 8   9   12  13  24  25  28  29  
# 10  11  14  15  26  27  30  31  
# 32  33  36  37  48  49  52  53  
# 34  35  38  39  50  51  54  55  
# 40  41  44  45  56  57  60  61  
# 42  43  46  47  58  59  62  63  

# 위치  (7,7) 은 63번째 방문
    
    
#아이디어 추출
# 배열을 4등분하여 재귀적으로 탐색
# 현재 배열 크기:  size = 2^N 
# 4개의 영역 구분:
# 	1) 1번 영역 (좌상단) → (0,0) ~  (size/2 - 1, size/2 - 1) 
# 	2) 2번 영역 (우상단) →  (0, size/2)  ~  (size/2 - 1, size - 1) 
# 	3) 3번 영역 (좌하단) →  (size/2, 0)  ~  (size - 1, size/2 - 1) 
# 	4) 4번 영역 (우하단) →  (size/2, size/2)  ~  (size - 1, size - 1) 
# 	5) (r,c) 의 위치에 따라 해당 영역으로 이동하면서 현재까지의 방문 횟수를 누적
 
#아이디어를 문제에 적용
# 재귀적으로 배열을 4등분하며 진행
# 	1) 현재 크기  size = 2^N 
# 	2) size 가 1이 될 때까지 반복
# 어떤 영역에 속하는지 판별
# 	1) 1번 영역 (좌상단):  r < size/2, c < size/2 
# 	2) 2번 영역 (우상단):  r < size/2, c \geq size/2 
# 	3) 3번 영역 (좌하단):  r \geq size/2, c < size/2 
# 	4) 4번 영역 (우하단):  r \geq size/2, c \geq size/2 
# 해당 영역에 속하는 만큼 방문 순서를 더하고 다음 크기로 이동
# 	1) 좌상단: 그대로 진행
# 	2) 우상단:  방문 순서 + (size/2 \times size/2) 
# 	3) 좌하단:  방문 순서 + 2 \times (size/2 \times size/2) 
# 	4) 우하단:  방문 순서 + 3 \times (size/2 \times size/2) 
 
import sys

def find_z_order(size_level, target_row, target_col, curr_row=0, curr_col=0, visit_count=0):

    if size_level == 0:
        return visit_count

    half_size = 2 ** (size_level - 1)  # 현재 분할된 정사각형 한 변의 절반 크기

    # 1번 영역 (좌상단)
    if target_row < curr_row + half_size and target_col < curr_col + half_size:
        return find_z_order(size_level - 1, target_row, target_col, curr_row, curr_col, visit_count)
    
    # 2번 영역 (우상단)
    elif target_row < curr_row + half_size and target_col >= curr_col + half_size:
        return find_z_order(size_level - 1, target_row, target_col, curr_row, curr_col + half_size, visit_count + half_size * half_size)
    
    # 3번 영역 (좌하단)
    elif target_row >= curr_row + half_size and target_col < curr_col + half_size:
        return find_z_order(size_level - 1, target_row, target_col, curr_row + half_size, curr_col, visit_count + 2 * half_size * half_size)
    
    # 4번 영역 (우하단)
    else:
        return find_z_order(size_level - 1, target_row, target_col, curr_row + half_size, curr_col + half_size, visit_count + 3 * half_size * half_size)

# 입력 받기
matrix_size, target_x, target_y = map(int, sys.stdin.readline().split())

# 탐색 시작
print(find_z_order(matrix_size, target_x, target_y))