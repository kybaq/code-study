from collections import deque

def solution(priorities, location):
    # 각 프로세스의 우선순위와 인덱스 큐에 넣기
    queue = deque()

    for index, priority in enumerate(priorities):
        queue.append((priority, index)) # 큐에 (우선순위, 인덱스) 형태로 저장
    
    order = 0  # 프로세스 실행 순서를 저장할 변수

    while queue:
        current = queue.popleft()  # 큐의 맨 앞 요소 꺼내기

        # 큐에 우선순위가 더 높은 프로세스가 있는지 확인
        if any(current[0] < process[0] for process in queue):
            # 우선순위가 더 높은 것이 있다면 다시 큐 맨 뒤에 추가
            queue.append(current)
        else:
            # 그렇지 않다면 현재 프로세스를 실행
            order += 1  # 실행 순서 +1
            
            # 내가 찾는 프로세스인지 확인
            if current[1] == location:
                # 내가 찾는 프로세스라면 실행 순서를 반환
                return order
