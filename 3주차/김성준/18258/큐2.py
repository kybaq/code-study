# 1. 문제 이해
# 큐는 FIFO(First In, First Out) 구조로 동작.
# 주어진 6가지 명령을 처리:
# 	1) push X: 정수 X를 큐에 삽입.
# 	2) pop: 큐에서 가장 앞에 있는 정수를 제거하고 출력. 큐가 비어있으면 -1 출력.
# 	3) size: 큐에 들어있는 정수의 개수 출력.
# 	4) empty: 큐가 비어있으면 1, 아니면 0 출력.
# 	5) front: 큐의 맨 앞 정수를 출력. 비어있으면 -1 출력.
# 	6) back: 큐의 맨 뒤 정수를 출력. 비어있으면 -1 출력.
 
 
#  2. 예제 이해
# 입력: 
# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front

# 처리 과정:
# 1) push 1 => 큐: [1]
# 2) push 2 => 큐: [1, 2]
# 3) front => 출력: 1 (맨 앞 값)
# 4) back => 출력: 2 (맨 뒤 값)
# 5) size => 출력: 2 (큐 크기)
# 6) empty => 출력: 0 (큐가 비어있지 않음)
# 7) pop => 출력: 1, 큐: [2]
# 8) pop => 출력: 2, 큐: []
# 9) pop => 출력: -1 (큐가 비어있음)
# 10) size => 출력: 0
# 11) empty => 출력: 1 (큐가 비어있음)
# 12) pop => 출력: -1
# 13) push 3 => 큐: [3]
# 14) empty => 출력: 0
# 15) front => 출력: 3

# 출력:
# 1
# 2
# 2
# 0
# 1
# 2
# -1
# 0
# 1
# -1
# 0
# 3  

# 3. 아이디어 추출
# 큐 자료구조 사용:
#   1) Python의 collections.deque를 활용.
# 	2) deque는 O(1)로 삽입 및 제거를 지원.
# 명령 처리:
# 	1) 입력 명령을 순차적으로 처리.
# 	2) push: append 사용.
# 	3) pop: popleft로 제거.
# 	4) 나머지 명령은 조건문으로 처리.
 
#4. 아이디어를 문제에 적용
# 큐 초기화:
# 1) deque 자료구조를 사용하여 큐를 초기화.
# 2) deque는 큐의 특성상 효율적으로 삽입과 삭제를 처리할 수 있음(O(1) 연산).
# 명령어 입력 처리:
# 1) sys.stdin.read로 한 번에 입력을 받아 처리 속도를 향상.
# 2) splitlines()로 명령어를 한 줄씩 분리.
# 3) 각 명령을 순차적으로 처리하며 결과를 리스트에 저장.
# 명령어별 동작 처리:
# 1) push X:
#   큐의 맨 뒤에 정수 X를 추가.
# 2) pop:
#   큐에서 맨 앞의 정수를 제거하고 출력.
#   큐가 비어 있으면 -1을 반환.
# 3) size:
#   큐의 현재 크기를 반환.
# 4) empty:
#   큐가 비어 있으면 1, 그렇지 않으면 0을 반환.
# 5) front:
#   큐의 맨 앞 정수를 반환.
#   큐가 비어 있으면 -1을 반환.
# 6) back:
#   큐의 맨 뒤 정수를 반환.
#   큐가 비어 있으면 -1을 반환.
# 결과 저장 및 출력:
#   각 명령어의 결과를 리스트에 저장(results).
#   결과 리스트를 한 번에 출력하여 효율성 유지.


import sys
from collections import deque

input = sys.stdin.read # 입력을 한 번에 읽기
commands = input().splitlines()  # 줄 단위로 나눔
queue = deque()  # 큐 초기화
results = []  # 결과 저장

for command in commands[1:]:
    if command.startswith("push"):
        queue.append(int(command.split()[1]))  # 정수를 추가
    elif command == "pop":
        results.append(queue.popleft() if queue else -1)
    elif command == "size":
        results.append(len(queue))
    elif command == "empty":
        results.append(0 if queue else 1)
    elif command == "front":
        results.append(queue[0] if queue else -1)
    elif command == "back":
        results.append(queue[-1] if queue else -1)

sys.stdout.write("\n".join(map(str, results)) + "\n")