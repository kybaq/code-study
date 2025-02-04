from collections import deque

def bfs(start, computers, visited):

    queue = deque([start])
    visited[start] = True  # 시작 컴퓨터 방문 표시

    while queue:
        node = queue.popleft()  # 현재 방문할 컴퓨터
        
        for neighbor, is_connected in enumerate(computers[node]):
            # 연결된 컴퓨터이면서 방문하지 않았다면 탐색
            if is_connected == 1 and not visited[neighbor]:
                visited[neighbor] = True  # 방문 처리
                queue.append(neighbor)  # 큐에 추가

def solution(n, computers):
    visited = [False] * n  # 방문 여부를 저장하는 리스트
    network_count = 0  # 네트워크 개수

    for i in range(n):  # 모든 컴퓨터를 확인
        if not visited[i]:  # 방문하지 않은 컴퓨터라면 새로운 네트워크 탐색 시작
            bfs(i, computers, visited)
            network_count += 1  # 네트워크 개수 증가

    return network_count  # 네트워크 개수 반환
