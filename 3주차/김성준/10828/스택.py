# 1. 문제 이해
# 스택을 구현하고, 주어진 명령을 처리하는 프로그램 작성
# 	명령어는 5가지:
# 	  1) push X: 정수 X를 스택에 추가.
# 	  2) pop: 스택의 가장 위 정수를 제거하고 출력. 스택이 비어있으면 -1 출력.
# 	  3) size: 스택에 들어있는 정수의 개수 출력.
# 	  4) empty: 스택이 비어있으면 1, 아니면 0 출력.
#     5) top: 스택의 가장 위 정수를 출력. 스택이 비어있으면 -1 출력.
 
# 2. 예제 이해

# 입력 1: 
# 14
# push 1
# push 2
# top
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
# top

# 처리 과정:
# 1) push 1 => 스택: [1]
# 2) push 2 => 스택: [1, 2]
# 3) top => 출력: 2
# 4) size => 출력: 2
# 5) empty => 출력: 0
# 6) pop => 출력: 2, 스택: [1]
# 7) pop => 출력: 1, 스택: []
# 8) pop => 출력: -1 (스택이 비어 있음)
# 9) size => 출력: 0
# 10) empty => 출력: 1
# 11) pop => 출력: -1 (스택이 비어 있음)
# 12) push 3 => 스택: [3]
# 13) empty => 출력: 0
# 14) top => 출력: 3    

# 출력:
# 2
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

# 3. 아이디어 추출
# 스택 초기화:
#   1) 리스트를 사용하여 스택 구현.
#   2) 스택의 기본 연산은 append와 pop.
# 명령 처리:
# 	1) 명령어를 반복문으로 처리.
# 각 명령어에 대해 조건문으로 로직 수행:
# 	1) push X: 스택에 X 추가.
# 	2) pop: 스택이 비어 있으면 -1 출력, 그렇지 않으면 pop.
# 	3) size: 스택의 크기 출력.
# 	4) empty: 스택이 비어 있으면 1, 아니면 0 출력.
# 	5) top: 스택이 비어 있으면 -1, 아니면 맨 위의 요소 출력.
# 결과 저장:
# 	1) 출력은 매번 하지 않고, 결과를 리스트에 저장한 뒤 한 번에 출력.
 
# 4. 아이디어를 문제에 적용
# 스택 초기화:
# 	1) 스택을 리스트로 초기화하여 필요한 데이터를 저장.
# 	2) list는 스택의 기본 연산인 append와 pop을 O(1) 시간 복잡도로 처리할 수 있음.
# 명령어 처리 루프:
# 	1) 입력받은 명령어를 한 줄씩 처리.
# 	2) 각 명령어에 따라 다른 동작을 수행하며, 조건문을 사용해 명령을 구분.
# 	3) push X: 값을 스택에 추가.
# 	4) pop: 스택이 비어 있으면 -1을 저장, 그렇지 않으면 스택의 가장 위 요소를 제거하고 저장.
# 	5) size: 스택의 크기를 계산하고 저장.
# 	6) empty: 스택이 비어 있는지 확인하고 1(비어 있음) 또는 0(비어 있지 않음)을 저장.
# 	7) top: 스택의 가장 위 요소를 반환하고, 비어 있으면 -1을 저장.
# 출력 결과 저장:
# 	1) 각 명령의 결과를 별도의 리스트(results)에 저장


import sys
input = sys.stdin.read  # 입력을 한 번에 읽기
commands = input().splitlines()  # 명령어를 줄 단위로 분리
n = int(commands[0])  # 명령어 개수

stack = []  # 스택 초기화
results = []  # 출력 결과 저장

for command in commands[1:]: # 첫 번째 줄은 명령어 개수이므로 제외하고 처리
    if "push" in command:  # push 명령 처리
        _, value = command.split()  # push와 값을 분리
        stack.append(int(value))  # 값을 스택에 추가
    elif command == "pop":  # pop 명령 처리
        results.append(stack.pop() if stack else -1)  # 스택이 비어있으면 -1
    elif command == "size":  # size 명령 처리
        results.append(len(stack))  # 스택 크기 출력
    elif command == "empty":  # empty 명령 처리
        results.append(0 if stack else 1)  # 비어있으면 1, 아니면 0
    elif command == "top":  # top 명령 처리
        results.append(stack[-1] if stack else -1)  # 스택의 맨 위 값 출력, 없으면 -1

# 결과를 한 번에 출력
sys.stdout.write("\n".join(map(str, results)) + "\n")