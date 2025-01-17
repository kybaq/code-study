# 큐를 구현하는 파이썬 내장 자료구조
# 양쪽에서 삽입/삭제가 빠르고 회전을 효율적으로 수정
from collections import deque

def josephus_problem(n, k):
    # 사람 번호 큐 생성
    queue = deque(range(1, n + 1))  # 1부터 N까지 숫자를 생성한 후 deque로 큐로 변환
    
    # 결과를 저장할 리스트
    result = []

    # 큐에서 K번째 사람 제거 반복
    while queue:
        # K-1번 회전
        queue.rotate(-(k - 1))
        # popleft()로 큐의 왼쪽 사람 제저하게 하여 K번째 사람 제거
        result.append(queue.popleft())

    # 문자열로 변환하고 ,로 각 숫자 구분해서 연결
    return f"<{', '.join(map(str, result))}>"

# N, K를 정수로 변환
n, k = map(int, input().split())

print(josephus_problem(n, k))
