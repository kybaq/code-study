#문제 이해
# 이 문제는 재귀 함수의 개념을 설명하는 챗봇의 출력을 구현하는 문제임
# 입력으로 재귀 호출 횟수 N이 주어지며, 챗봇은 특정 패턴을 따라 재귀적으로 질문과 대답을 반복한다. 핵심은 들여쓰기(`____`)를 이용해 재귀 깊이를 표현

#예제 이해
# 1) 첫 번째 줄에서 학생이 교수님께 질문
# 2) 이후 `재귀함수가 뭔가요?`라는 질문이 반복되며, 재귀 깊이에 따라 `____` 들여쓰기가 추가
# 3) 깊이가 `N`에 도달하면 `"재귀함수는 자기 자신을 호출하는 함수라네"`라는 정답을 출력
# 4) 이후 재귀가 종료되며 `"라고 답변하였지."`라는 문장이 각 깊이에 맞게 출력

#아이디어 창출
# 재귀를 사용
# 	1) 같은 질문이 반복되며, 깊이가 증가할 때마다 들여쓰기가 추가됨
# 	2) 따라서 depth 값을 활용하여 들여쓰기를 관리하면서 재귀 호출을 수행
# 기저 조건(Base Case)을 설정
# 	1) depth == N이 되면 "재귀함수는 자기 자신을 호출하는 함수라네"를 출력하고 종료
# 재귀 호출 수행
# 	1) "재귀함수가 뭔가요?"를 출력
# 	2) "잘 들어보게..." 설명을 출력
# 	3) depth + 1을 증가시켜 재귀적으로 같은 패턴을 호출
# 재귀가 종료되면서 "라고 답변하였지."를 출력
#   1) 재귀가 끝나고 돌아올 때 "라고 답변하였지."를 depth에 맞춰 출력

#아이디어를 문제에 적용
# 1) 먼저, `N`을 입력받음
# 2) "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."를 출력
# 3) 재귀 함수를 정의하여 `depth`를 매개변수로 받기
# 4) `depth`에 맞게 들여쓰기를 설정하여 `"재귀함수가 뭔가요?"`를 출력
# 5) 만약 `depth == N`이라면, `"재귀함수는 자기 자신을 호출하는 함수라네"`를 출력하고 종료
# 6) 그렇지 않다면, `"잘 들어보게..."`부터 `"그의 답은 대부분 옳았다고 하네..."`까지 설명을 출력
# 7) `depth + 1`을 인자로 하여 재귀 호출을 수행
# 8) 재귀 호출이 끝난 후 `"라고 답변하였지."`를 출력하여 재귀 종료를 처리


def chatbot(depth, n):
    indent = "____" * depth
    print(f'{indent}"재귀함수가 뭔가요?"')
    
    if depth == n:
        print(f'{indent}"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(f'{indent}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(f'{indent}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{indent}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        chatbot(depth + 1, n)
    
    print(f'{indent}라고 답변하였지.')

N = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot(0, N)