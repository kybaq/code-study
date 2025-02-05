#문제 이해
# 	1) 컴퓨터 간 네트워크 연결 상태가 2차원 배열(computers)로 주어짐.
# 	2) 연결된 컴퓨터들은 하나의 네트워크로 간주하며, 연결된 네트워크 개수를 찾아야 함.
# 	3) computers[i][j] = 1이면 i번 컴퓨터와 j번 컴퓨터가 직접 연결됨.
# 	4) computers[i][i] = 1이므로 자기 자신과는 항상 연결되어 있음.
# 	5) 모든 컴퓨터는 0부터 n-1까지 정수로 표현됨.

#예제 분석
# 입력 예시1
# n = 3
# computers = [[1, 1, 0], 
#              [1, 1, 0], 
#              [0, 0, 1]]
# 	1) 컴퓨터 0과 1이 서로 연결되어 있으므로 같은 네트워크
# 	2) 컴퓨터 2는 다른 컴퓨터와 연결되지 않으므로 독립된 네트워크
# 총 네트워크 개수는 2
 
# 입력 예시2
# n = 3
# computers = [[1, 1, 0], 
#              [1, 1, 1], 
#              [0, 1, 1]]
# 	1) 컴퓨터 0 => 1, 컴퓨터 1 => 2로 연결
# 	2) 모든 컴퓨터가 연결되어 하나의 네트워크 형성
# 	3) 총 네트워크 개수는 1

#아이디어 추출
# 네트워크 탐색을 위한 그래프 개념 활용
# 	1) 각 컴퓨터를 노드로, 연결 상태를 나타내는 computers[i][j] 값을 간선으로 생각
# 	2) 연결된 컴퓨터들을 하나의 네트워크로 그룹화해야 함
# 	3) 따라서, BFS(너비 우선 탐색)를 활용하여 한 번 탐색할 때마다 하나의 네트워크를 완전히 찾을 수 있음
# BFS(너비 우선 탐색) 활용 이유
# 	1) 모든 컴퓨터를 방문하면서 연결된 그룹을 찾아야 하므로 BFS 방식 적합
# 	2) 한 번 BFS를 수행할 때마다 하나의 네트워크가 탐색 완료됨
# 	3) 큐(queue)를 활용하여 방문할 컴퓨터를 관리하고, 중복 방문 방지를 위해 방문 여부를 저장

#아이디어를 문제에 적용

# 모든 컴퓨터를 순회하며 방문 여부를 확인
# 	1) is_checked 리스트를 사용하여 방문한 컴퓨터를 추적
# 	2) 방문하지 않은 컴퓨터를 발견하면 새로운 네트워크로 인식하고 BFS 탐색 시작
# BFS 탐색을 통해 하나의 네트워크를 탐색
# 	1) queue를 활용하여 연결된 모든 컴퓨터를 탐색
# 	2) computers[i][j] == 1 이고 방문하지 않은 경우 queue에 추가
# 모든 컴퓨터를 확인한 후, 네트워크 개수 반환
# 	1) BFS를 수행할 때마다 하나의 네트워크가 완전히 탐색됨
# 	2) BFS 실행 횟수만큼 네트워크 개수를 증가시키고 최종 반환



from collections import deque

def explore_network(start, computers, is_checked):
    """BFS 방식으로 네트워크 탐색"""
    queue = deque([start])
    is_checked[start] = True  # 현재 컴퓨터 방문 처리

    while queue:
        current_computer = queue.popleft()  # 현재 방문 중인 컴퓨터
        
        # 모든 컴퓨터를 순회하며 연결된 컴퓨터 탐색
        for next_computer in range(len(computers)):  
            if computers[current_computer][next_computer] == 1 and not is_checked[next_computer]:  
                is_checked[next_computer] = True  # 방문 처리
                queue.append(next_computer)  # 큐에 추가하여 다음 탐색

def count_isolated_networks(n, computers):

    is_checked = [False] * n  # 방문 여부 체크 배열
    total_networks = 0  # 네트워크 개수 카운트

    for computer in range(n):  # 모든 컴퓨터를 확인
        if not is_checked[computer]:  # 방문하지 않은 경우 새로운 네트워크 시작
            explore_network(computer, computers, is_checked)
            total_networks += 1  # 네트워크 개수 증가

    return total_networks  # 네트워크 개수 반환