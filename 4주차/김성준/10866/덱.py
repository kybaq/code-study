# 1.문제 이해
# 정수를 저장하는 덱을 직접 구현한 뒤, 주어지는 명령을 처리하여 결과를 출력
# 주요 명령 :
# push_front X: 정수 X를 덱의 앞에 삽입
# push_back X: 정수 X를 덱의 뒤에 삽입
# pop_front: 덱의 가장 앞에 있는 정수를 제거하고 출력. 덱이 비어 있으면 -1 출력
# pop_back: 덱의 가장 뒤에 있는 정수를 제거하고 출력. 덱이 비어 있으면 -1 출력
# size: 덱에 들어있는 정수의 개수를 출력
# empty: 덱이 비어 있으면 1, 아니면 0 출력
# front: 덱의 가장 앞에 있는 정수를 출력. 비어 있으면 -1 출력
# back: 덱의 가장 뒤에 있는 정수를 출력. 비어 있으면 -1 출력
 
# 2.예제 이해
# 입력
# 15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front

# 처리과정
# 1) push_back 1 => 덱: [1]
# 2) push_front 2 => 덱: [2, 1]  (앞에 2 추가)
# 3) front => 출력: 2 (덱 맨 앞)
# 4) back => 출력: 1 (덱 맨 뒤)
# 5) size => 출력: 2
# 6) empty => 출력: 0 (비어 있지 않음)
# 7) pop_front => 출력: 2, 덱: [1]
# 8) pop_back => 출력: 1, 덱: []
# 9) pop_front => 덱이 비었으므로 출력: -1
# 10) size => 출력: 0
# 11) empty => 출력: 1 (비어 있음)
# 12) pop_back => 출력: -1 (비어 있음)
# 13) push_front 3 => 덱: [3]
# 14) empty => 출력: 0 (비어 있지 않음)
# 15) front => 출력: 3
# 출력
# 2
# 1
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3

# 3.아이디어 추출
# 파이썬에서는 collections.deque를 활용하면 덱 연산을 O(1)에 가깝게 처리 가능
# 직접 리스트로 구현해도 되지만, 양쪽에 데이터를 삽입/삭제해야 하므로 deque가 적합
# 명령어에 따른 처리:
# 	1) push_front X: 덱의 앞에 X 삽입
# 	2) push_back X: 덱의 뒤에 X 삽입
# 	3) pop_front: 덱의 앞에서 원소 제거 후 출력 (없으면 -1)
# 	4) pop_back: 덱의 뒤에서 원소 제거 후 출력 (없으면 -1)
# 	5) size: 덱의 길이 출력
# 	6)empty: 길이가 0이면 1, 아니면 0 출력
# 	7) front: 덱의 맨 앞 원소 출력 (없으면 -1)
# 	8) back: 덱의 맨 뒤 원소 출력 (없으면 -1)
# 출력 방식:
# 문제의 처리 속도를 고려해, 결과를 문자열로 누적 후 한 번에 출력하는 방식을 사용할 수 있음
 
# 4.아이디어를 문제에 적용
# 데이터 구조 초기화
# 명령어 반복 처리
# 	1) 입력으로 주어진 N번의 명령을 반복하며 다음을 수행
# 	2) 명령어를 문자열로 입력받아 공백을 기준으로 나눈 뒤, 첫 번째 토큰으로 분기 처리
# 조건문으로 세부 로직 구현
# 	1) pop_front: 덱이 비었는지 먼저 확인 후, 비어 있으면 -1 출력, 아니면 popleft()
# 	2) pop_back: 덱이 비었는지 먼저 확인 후, 비어 있으면 -1 출력, 아니면 pop()
# 	3) size: len(dq) 출력
# 	4) empty: 비었으면 1, 아니면 0
# 	5) front: 비었으면 -1, 아니면 dq[0]
# 	6) back: 비었으면 -1, 아니면 dq[-1]
# 결과 출력 방식
#   1) 각 명령어마다 출력이 필요한 경우(예: pop, size, empty, front, back) 그 결과를 변수에 담아서 print
# 	2) 많은 데이터를 처리할 때는 sys.stdin.readline과 sys.stdout.write를 사용할 수 있지만, 기본 input()과 print()로도 충분히 처리 가능 (명령 수가 10,000개이므로 크게 문제되지 않음)

import sys
from collections import deque

# 명령의 수 N을 입력받는다.
n = int(sys.stdin.readline())

# 덱 초기화
d = deque()

for _ in range(n):
    # 한 줄씩 명령어를 입력받아 공백으로 분리한다.
    c = sys.stdin.readline().split()
    
    # 명령에 따라 분기 처리
    if c[0] == 'push_front':
        # 덱의 앞에 c[1]을 삽입
        d.appendleft(c[1])
    elif c[0] == 'push_back':
        # 덱의 뒤에 c[1]을 삽입
        d.append(c[1])
    elif c[0] == 'pop_front':
        # 덱이 비어있다면 -1, 아니면 앞의 원소를 꺼내서 출력
        print(d.popleft() if d else -1)
    elif c[0] == 'pop_back':
        # 덱이 비어있다면 -1, 아니면 뒤의 원소를 꺼내서 출력
        print(d.pop() if d else -1)
    elif c[0] == 'size':
        # 덱에 들어있는 원소의 개수 출력
        print(len(d))
    elif c[0] == 'empty':
        # 덱이 비어있으면 1, 아니면 0 출력
        print(0 if d else 1)
    elif c[0] == 'front':
        # 덱이 비어있으면 -1, 아니면 맨 앞 원소 출력
        print(d[0] if d else -1)
    elif c[0] == 'back':
        # 덱이 비어있으면 -1, 아니면 맨 뒤 원소 출력
        print(d[-1] if d else -1)