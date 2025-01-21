# 스택에 여는 괄호만 모두 저장
# 닫는 괄호가 들어올 때 여는 괄호 삭제
# 스택이 비어있는데 닫는 괄호가 들어온다면 False 반환
# 다 돌고도 뭐가 남아 있으면 False 반환
def solution(s):
    stack = []  # 여는 괄호를 저장할 스택

    for char in s:  # 문자열을 한 문자씩 순회하며
        if char == '(':  
            stack.append(char) # 스택에 '(' 만 저장
        else:  # 닫는 괄호일 경우
            if stack:  # 스택이 비어있지 않다면
                stack.pop()  # 스택에서 여는 괄호 하나 제거
            else:  
                return False  # 스택이 비어있으면 짝이 맞지 않음
    
    return len(stack) == 0  # 모든 작업 후 스택이 비어있으면 True
