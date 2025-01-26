from collections import deque

def rotating_queue():

    n, m = map(int, input().split())  # 큐의 크기 n과 뽑아낼 원소의 개수 m
    targets = list(map(int, input().split()))  # 뽑아낼 원소의 위치 목록

    queue = deque(range(1, n + 1))  # 1부터 n까지의 숫자로 이루어진 deque 생성
    operations = 0  # 2번과 3번 연산의 총 횟수

    for target in targets:
        while True:
            if queue[0] == target:  # 큐의 첫 번째 원소가 뽑아내려는 원소라면
                queue.popleft()  # 첫 번째 원소를 제거
                break  # 다음 원소로 넘어감
            else:
                # 뽑아내려는 원소의 위치를 기준으로 왼쪽/오른쪽 회전을 결정
                target_index = queue.index(target)  # 타겟 원소의 현재 위치
                if target_index <= len(queue) // 2:  # 왼쪽으로 회전하는 것이 더 빠름
                    queue.rotate(-1)  # 왼쪽으로 한 칸 이동
                    operations += 1
                else:  # 오른쪽으로 회전하는 것이 더 빠름
                    queue.rotate(1)  # 오른쪽으로 한 칸 이동
                    operations += 1

    print(operations)

rotating_queue()
