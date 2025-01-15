def solution(n, left, right):
    """
    1. n x n의 2차원 배열
    2. i = 1 ~ n에 대해 1.1부터 i.i까지 모든 빈 칸을 i
    3. 1 ~ n까지 잘라서 모두 붙인 새 1차원 배열
    4. 새 1차원 배열을 arr라 하고, arr[left] ~ arr[right]만 남기고 지우기

    가로 길이가 n인 2차원 배열을 일렬로 나열했을 때 row = i / n, col = i % n
    한 행에 n칸이 있고 1차원 인덱스 i에서 i / n은 건너뛴 행의 갯수, i % n은 나머지로 그 행에서의 위치를 나타내니까
    """
    answer = []

    # left부터 right까지 반복하기 위해서 left, right + 1
    for i in range(left, right + 1):
        # i번째 원소가 몇 번째 행인지 확인
        row = i // n
        # i번째 원소가 그 행에서 몇 번째 열인지 확인
        col = i % n
        # i는 1부터 시작되니 최댓값에 +1을 해야 맞는 인덱스
        val = max(row, col) + 1
        # answer에 val값들을 넣으면 정답 배열
        answer.append(val)

    return answer

