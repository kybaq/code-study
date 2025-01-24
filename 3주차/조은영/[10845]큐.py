from collections import deque
import sys
input = sys.stdin.read

def main():
    commands = input().splitlines()
    n = int(commands[0])  # 명령의 수
    queue = deque()
    results = []

    for i in range(1, n + 1):
        command = commands[i]

        if command.startswith("push"):
            _, x = command.split()
            queue.append(int(x))
        
        elif command == "pop":
            if queue:
                results.append(queue.popleft())
            else:
                results.append(-1)
        
        elif command == "size":
            results.append(len(queue))
        
        elif command == "empty":
            results.append(1 if not queue else 0)
        
        elif command == "front":
            if queue:
                results.append(queue[0])
            else:
                results.append(-1)
        
        elif command == "back":
            if queue:
                results.append(queue[-1])
            else:
                results.append(-1)

    # 결과 출력
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
