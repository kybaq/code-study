def solution(prices):
    n = len(prices)  # 주식 가격 배열의 길이 계산
    answer = [0] * n  # 각 시점의 결과를 저장할 리스트
    stack = []  # 주식 가격 인덱스 저장

    for i in range(n):
        # 현재 가격이 스택의 top 인덱스에 해당하는 가격보다 낮다면 루프
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop() #top(마지막 인덱스) 꺼내고, 가격 떨어지는 시점 결정된 주식 가격 인덱스
            answer[top] = i - top  # 떨어지기까지 걸린 시간 계산
        stack.append(i)  # 현재 인덱스를 스택에 추가(아직 안떨어짐)

    # 스택에 남아 있는 인덱스 처리
    while stack:
        top = stack.pop()
        answer[top] = n - top - 1  # 끝까지 떨어지지 않은 시간 계산

    return answer
