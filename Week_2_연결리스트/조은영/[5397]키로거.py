# 기본적으로 문자는 입력되면 왼쪽 스택으로
# 왼쪽 화살표는 '<' 왼쪽 스택의 문자를 오른쪽 스택에 옮겨줌, 오른쪽은 반대
# '-'는 왼쪽 스택에서 문자 삭제
# 마지막으로 오른쪽 스택 뒤집어서 왼족에 붙이기

# 화살표보고 인덱스 이동해서 문자도 옮겨준다고 생각했는데 두 개의 스택을 선언해서 푸는게 쉽게 풀리는 방법이었다
import sys
input = sys.stdin.readline

# 테스트케이스 갯수 받아서 정수형 변환 -> n에 저장
n = int(input())

for i in range(n):
    # 양쪽 공백 빼고 하나하나 리스트로 password에 저장
    password = list(input().strip())
    # 커서의 왼쪽, 오른쪽 두 개의 스택을 사용하는 게 킥..,
    left, right = [], []

    for j in password:
        if j == '<':
            if left:  # left가 비어있지 않으면, 즉 커서의 왼쪽에 문자가 존재 -> 커서 이동
                right.append(left.pop())
        elif j == '>':
            if right:  # 커서의 오른쪽에 문자 존재 -> 커서 이동
                left.append(right.pop())
        elif j == '-':
            if left:  # 리스트 마지막 문자 제거 -> 백스페이스
                left.pop()
        else:
            left.append(j) # 일반 문자 입력이니 left리스트에 추가

    left.extend(reversed(right)) # right 배열은 실제 문자열과 반대 정렬이므로 다시 뒤집어서 붙여야함

    print(''.join(left))