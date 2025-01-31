import sys
from collections import deque

input = sys.stdin.readline

d = deque()

N = int(input())

result = []

for _ in range(N):
    command = input().split()

    # 덱 앞에 X 추가
    if command[0] == "1":
        d.appendleft(command[1])

    # 덱 뒤에 X 추가
    elif command[0] == "2":
        d.append(command[1])

    # 덱 맨 앞 원소 제거 후 출력, 없으면 -1
    elif command[0] == "3":
        result.append(d.popleft() if d else "-1")

    # 덱 맨 뒤 원소 제거 후 출력, 없으면 -1
    elif command[0] == "4":
        result.append(d.pop() if d else "-1")

    # 덱 크기 출력
    elif command[0] == "5":
        result.append(str(len(d)))

    # 덱이 비었으면 1, 아니면 0
    elif command[0] == "6":
        result.append("1" if not d else "0")

    # 덱 맨 앞 원소 출력, 없으면 -1
    elif command[0] == "7":
        result.append(d[0] if d else "-1")

    # 덱 맨 뒤 원소 출력, 없으면 -1
    elif command[0] == "8":
        result.append(d[-1] if d else "-1")

sys.stdout.write("\n".join(result) + "\n")
