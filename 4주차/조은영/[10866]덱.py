from collections import deque
import sys

# 명령의 수 입력 받기
n = int(sys.stdin.readline())

d = deque()

for _ in range(n):
    command = sys.stdin.readline().split()  # 한 줄씩 명령어 입력받기

    if command[0] == "push_front": 
        d.appendleft(command[1])  # 덱의 앞에 정수 X 삽입
    elif command[0] == "push_back":
        d.append(command[1])  # 덱의 뒤에 정수 X 삽입
    elif command[0] == "pop_front":
        # 덱이 비어있으면 -1, 아니면 맨 앞 원소 제거한 후 출력
        print(d.popleft() if d else -1)
    elif command[0] == "pop_back": 
        # 덱이 비어있으면 -1, 아니면 맨 뒤 원소 제거한 후 출력
        print(d.pop() if d else -1)
    elif command[0] == "size":
        print(len(d))  # 덱의 원소 개수 출력
    elif command[0] == "empty": 
        print(0 if d else 1)  # 덱 비어있으면 1, 아니면 0 출력
    elif command[0] == "front": 
        # 덱이 비어있으면 -1, 아니면 맨 앞 정수 출력
        print(d[0] if d else -1)
    elif command[0] == "back": 
        # 덱이 비어있으면 -1, 아니면 맨 뒤 정수 출력
        print(d[-1] if d else -1)
