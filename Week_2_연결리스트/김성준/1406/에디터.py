# 1. 문제 이해

# 주어진 초기 문자열과 명령어 리스트를 통해서 편집기가 작성한 최종 문자열을 구하는 프로그램을 작성
# 편집기의 동작 
# 문자열은 최대 600,000자까지 입력 가능
# 커서의 위치는 문자열 맨 앞, 맨 뒤, 또는 중간에 위치할 수 있음
# 커서 이동 및 문자열 수정은 다음 명령어를 통해 수행:
# L: 커서를 왼쪽으로 한 칸 이동 (맨 앞이면 무시)
# D: 커서를 오른쪽으로 한 칸 이동 (맨 뒤면 무시)
# B: 커서 왼쪽 문자를 삭제 (맨 앞이면 무시)
# P $: 커서 왼쪽에 문자 $를 삽입
# 초기 조건: 명령어 수행 전 커서는 문장의 맨 뒤에 위치
# 출력값: 모든 명령어를 수행한 후 최종 문자열


#  2. 예제 이해
# abcd
# 3
# P x
# L
# P y

# 명령어 수행 과정
# 1) 초기 상태: 문자열 abcd (커서는 맨 뒤에 위치)
# 2) 명령어 P x: x를 커서 왼쪽에 삽입 → abcdx (커서는 x 뒤에 위치)
# 3) 명령어 L: 커서를 왼쪽으로 이동 → abcd|x (커서는 d와 x 사이에 위치)
# 4) 명령어 P y: y를 커서 왼쪽에 삽입 → abcdyx (커서는 y 뒤에 위치)

# 최종출력
# abcdyx


# 3. 아이디어 추출
#   1) 리스트로 문자열 처리:
#       문자열을 리스트 두 개로 관리
#       왼쪽 리스트: 커서 왼쪽의 모든 문자
#       오른쪽 리스트: 커서 오른쪽의 모든 문자
#       커서 이동 및 삽입/삭제가 리스트의 끝에서 일어나므로 스택처럼 동작해 O(1) 시간에 처리 가능
#   2) 명령어 처리:
#       L: 오른쪽 리스트의 첫 문자를 왼쪽 리스트로 이동
#       D: 왼쪽 리스트의 마지막 문자를 오른쪽 리스트로 이동
#       B: 왼쪽 리스트의 마지막 문자를 삭제
#       P $: $를 왼쪽 리스트의 끝에 추가
#   3) 최종 결과 생성:
#    모든 명령어 수행 후, 왼쪽 리스트와 오른쪽 리스트를 합쳐 최종 문자열 생성
 
 
#  4. 문제에 아이디어 접목
#   1) 초기 문자열을 입력받아 왼쪽 리스트에 저장
#   2) 명령어를 하나씩 읽어 리스트를 수정
#   3) 명령어 처리가 끝난 뒤, 왼쪽 리스트와 오른쪽 리스트를 합쳐 출력

from collections import deque
import sys

def editor(initial_string, commands):
    
    # 왼쪽과 오른쪽을 deque로 초기화
    left = deque(initial_string)
    right = deque()

    for command in commands:
        if command[0] == 'L':  # 커서를 왼쪽으로 이동
            if left:
                right.appendleft(left.pop())
        elif command[0] == 'D':  # 커서를 오른쪽으로 이동
            if right:
                left.append(right.popleft())
        elif command[0] == 'B':  # 왼쪽 문자 삭제
            if left:
                left.pop()
        elif command[0] == 'P':  # 왼쪽에 문자 삽입
            left.append(command[1])

    # 최종 문자열 생성
    return ''.join(left) + ''.join(right)

# 입력 처리
input = sys.stdin.read  # sys.stdin.read()를 사용해 입력 처리
data = input().splitlines()  # 전체 입력 읽기
initial_string = data[0]
n = int(data[1])
commands = [line.split() for line in data[2:]]

# 결과 출력
print(editor(initial_string, commands))