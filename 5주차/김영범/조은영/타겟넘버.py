# 재귀 탐색 함수
def dfs(numbers, target, index, current_sum):

    # 모든 숫자를 사용한 경우
    if index == len(numbers):
        #현재까지의 합이 target과 같다면 1을 반환
        return 1 if current_sum == target else 0

    # 현재 숫자를 더하는 경우 + 빼는 경우 두 가지 탐색
    return (dfs(numbers, target, index + 1, current_sum + numbers[index]) +
            dfs(numbers, target, index + 1, current_sum - numbers[index]))

def solution(numbers, target):
    # DFS 탐색 시작 인덱스, 초기 합 0
    return dfs(numbers, target, 0, 0)
