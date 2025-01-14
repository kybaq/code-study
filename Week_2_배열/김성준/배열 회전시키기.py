# 1. 문제 이해
# 	배열의 원소를 “left” 또는 “right” 방향으로 한 칸씩 회전시켜야 함


#  2. 예제 분석

# 예제1
# 	1) 입력값: numbers = [1, 2, 3], direction = "right"
# 	2) 출력값: [3, 1, 2]
# 예제2
#   1) 입력값: numbers = [4, 455, 6, 4, -1, 45, 6], direction = "left"
# 	2) 출력값: [455, 6, 4, -1, 45, 6, 4]

 
#  3. 아이디어 접목

# 	1.	“left”와 “right” 방향 처리:
# 	  1) “left”: 배열의 첫 번째 요소를 잘라서 맨 뒤에 붙임
# 	  2) “right”: 배열의 마지막 요소를 잘라서 맨 앞으로 붙임
# 	2.	슬라이싱 활용:
# 	  1) 배열을 슬라이싱하여 회전 처리 가능:
# 	  2) “left”: numbers[1:] + numbers[:1]
# 	  3) “right”: numbers[-1:] + numbers[:-1]
# 	3.	조건문 사용:
# 	  1) if 조건문으로 direction 값에 따라 슬라이싱 방식 결정
# 	4.	결과 반환:
# 	  1) 슬라이싱 결과를 반환


def solution(numbers, direction):
    # "left" 방향 처리
    if direction == "left":
        # 배열의 첫 번째 요소를 제외한 나머지(numbers[1:])를 앞에 두고,
        # 첫 번째 요소(numbers[:1])를 뒤에 붙여 새로운 배열 생성
        return numbers[1:] + numbers[:1]

    # "right" 방향 처리
    elif direction == "right":
        # 배열의 마지막 요소(numbers[-1:])를 앞에 두고,
        # 나머지 요소(numbers[:-1])를 뒤에 붙여 새로운 배열 생성
        return numbers[-1:] + numbers[:-1]