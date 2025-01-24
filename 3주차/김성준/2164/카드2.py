#1.문제 이해
# N장의 카드는 1번부터 N번까지 번호가 붙어 있고, 1번 카드가 가장 위에, N번 카드가 가장 아래에 위치
# 아래 동작을 카드가 한 장 남을 때까지 반복:
#   1) 제일 위의 카드를 버린다
#   2) 남은 카드 중 제일 위의 카드를 제일 아래로 옮긴다
# 마지막에 남는 카드의 번호를 구하는 문제
 
#2.예제 이해

# 예제1: N = 6
# 초기 상태: [1, 2, 3, 4, 5, 6]
# 	1) 1을 버림 → [2, 3, 4, 5, 6]
# 	2) 2를 아래로 이동 → [3, 4, 5, 6, 2]
# 	3) 3을 버림 → [4, 5, 6, 2]
# 	4) 4를 아래로 이동 → [5, 6, 2, 4]
# 	5) 5를 버림 → [6, 2, 4]
# 	6) 6을 아래로 이동 → [2, 4, 6]
# 	7) 2를 버림 → [4, 6]
# 	8) 4를 아래로 이동 → [6, 4]
# 	9) 6을 버림 → [4]
# 	10) 마지막 남은 카드: 4

 
#3.아이디어 정리
# 큐를 사용:
#   1) deque 자료구조를 활용하여 카드를 관리
# 	2) 카드의 맨 위와 맨 아래를 빠르게 처리
# 과정 구현:
# 	1) 큐의 맨 앞에서 카드를 버림 (popleft)
# 	2) 큐의 맨 앞 카드를 맨 뒤로 이동 (append)
# 종료 조건:
# 	1) 큐에 카드가 1장 남을 때 종료
# 시간 복잡도:
# 	각 연산은 O(1)이며, N장의 카드를 처리하므로 전체 시간 복잡도는 O(N)
 
#4.아이디어를 문제에 적용
# 큐 초기화:
# 	1) 1번부터 N번까지의 번호를 deque로 저장하여 큐를 초기화.
# 카드 처리:
#   1) 큐에서 맨 위의 카드를 제거 => popleft()
#   2) 그다음 맨 위의 카드를 맨 아래로 이동 => append()
# 종료:
#   1) 큐에 남아 있는 카드가 1장이 되면 반복을 종료
# 결과 출력:
#   1) 큐에 남아 있는 마지막 카드 번호를 출력
 
from collections import deque

# 큐 초기화: 1번부터 N번까지의 번호를 deque로 저장
N = int(input().strip())
queue = deque(range(1, N + 1))

# 카드 처리: 큐에 카드가 1장 남을 때까지 반복
while len(queue) > 1:
    queue.popleft() 
    queue.append(queue.popleft()) 

# 3. 종료: 큐에 남아 있는 마지막 카드 번호 출력
print(queue[0])