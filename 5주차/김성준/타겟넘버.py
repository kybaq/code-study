#문제 이해
# 주어진 numbers 배열의 각 숫자를 + 또는 -로 조합하여 target 값을 만드는 방법의 개수를 구하는 문제
# 연산 순서는 바꿀 수 없으며, 숫자는 주어진 순서대로만 사용 가능
 
#예제 이해
# 입력: numbers = [1, 1, 1, 1, 1], target = 3
 
#  -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# 출력: 5
 
#아이디어 추출
# 모든 숫자에 +와 -를 붙이는 경우를 고려해야 하므로 DFS (깊이 우선 탐색) 또는 BFS (너비 우선 탐색)가 적합함
# queue를 사용하여 모든 가능한 합을 탐색하면서 target과 일치하는 경우의 개수를 세기
# 탐색 방식:
#   1) 초기 상태 (index = 0, sum = 0) 를 queue에 삽입
#   2) queue에서 원소를 꺼내, 다음 숫자를 + 또는 -로 적용한 두 가지 경우를 다시 queue에 삽입
#   3) 모든 숫자를 다 사용했을 때(index == len(numbers)), target과 일치하면 카운트 증가
#   4) 모든 경우를 탐색한 후, 최종적으로 target과 일치하는 경우의 개수를 반환
 
#아이디어를 문제에 적용
# 1) BFS를 활용하여 큐(queue) 에 (현재 index, 현재까지의 합) 형태의 데이터를 저장하고 탐색
# 2) 큐에서 데이터를 하나씩 꺼내면서 + 또는 - 연산을 수행하여 다음 단계의 값을 큐에 추가
# 3) 모든 숫자를 사용한 경우(index == len(numbers))에 target과 일치하는지 검사하여 카운트 증가
# 4) 최종적으로 queue가 빌 때까지 모든 경우를 탐색한 후, target과 일치한 개수를 반환
 
 
from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (현재 인덱스, 현재 합)
    count = 0

    while queue:
        index, current_sum = queue.popleft()

        # 1. 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            # 2. 현재 숫자를 더하거나 빼는 두 가지 경우 큐에 추가
            queue.append((index + 1, current_sum + numbers[index]))
            queue.append((index + 1, current_sum - numbers[index]))

    return count