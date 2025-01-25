from collections import deque
import sys

def main():
    input = sys.stdin.read  # 입력 읽어오기
    commands = input().splitlines()  # 줄 단위로 나눈 다음 명령으로 변환
    n = int(commands[0])  # 첫 번째 줄에 주어진 명령의 개수
    queue = deque()  # deque로 생성
    results = []

    for i in range(1, n + 1):  # 두 번째 줄부터 명령 시작
        command = commands[i]

        if command.startswith("push"):
            _, x = command.split()  # 명령어와 숫자를 분리
            queue.append(int(x))  # 숫자를 큐의 뒤에 추가

        elif command == "pop":
            if queue:  # 큐가 비어있지 않으면
                results.append(queue.popleft())  # 맨 앞의 값을 제거하고 저장
            else:  # 큐가 비어있으면
                results.append(-1)  # -1 저장

        elif command == "size":
            results.append(len(queue))  # 큐의 크기를 저장

        elif command == "empty":
            results.append(1 if not queue else 0)  # 비어있으면 1, 아니면 0 저장

        elif command == "front":
            if queue:  # 큐가 비어있지 않으면
                results.append(queue[0])  # 맨 앞의 값을 저장
            else:  # 큐가 비어있으면
                results.append(-1)  # -1 저장

        elif command == "back":
            if queue:  # 큐가 비어있지 않으면
                results.append(queue[-1])  # 맨 뒤의 값을 저장
            else:  # 큐가 비어있으면
                results.append(-1)  # -1 저장

    sys.stdout.write("\n".join(map(str, results)) + "\n")  # 결과 리스트를 줄 바꿈으로 연결해 출력
main()
