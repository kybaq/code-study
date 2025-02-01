#문제 이해
# 주어진 문자열에서 괄호의 균형이 맞는지 판별해야 한다.
# 사용되는 괄호 종류는 소괄호 ()와 대괄호 [] 두 가지이다.
# 균형을 이루는 조건:
# 	1) 각 열린 괄호는 반드시 닫는 괄호가 있어야 함
# 	2) 소괄호 ()는 같은 종류끼리 짝을 이뤄야 함
# 	3) 대괄호 []도 같은 종류끼리 짝을 이뤄야 함
# 	4) 괄호 안의 문자열도 균형이 잡혀 있어야 함
# 마지막에 입력 종료 조건으로 .(온점)이 주어짐
# 균형이 맞으면 "yes", 균형이 깨지면 "no"를 출력해야 함

#예제 이해
# 입력: So when I die (the [first] I will see in (heaven) is a score list).
# ( 와 ) 짝이 맞음
# [ 와 ] 짝이 맞음
# 괄호 안의 내용도 균형을 유지하므로 "yes"
# 출력: yes

# 입력: [ first in ] ( first out ).
# [ 와 ] 짝이 맞음
# ( 와 ) 짝이 맞음
# 괄호 안의 내용도 균형을 유지하므로 "yes"
# 출력: yes
 
# 입력: Half Moon tonight (At least it is better than no Moon at all].
# ( 와 )는 짝이 맞음
# 하지만, [ 가 닫히지 않음 → "no"
# 출력: no
         
# 입력: A rope may form )( a trail in a maze.
# )( 순서가 잘못됨 (닫는 괄호가 먼저 나옴) → "no"
# 출력: no

# 입력: Help( I[m being held prisoner in a fortune cookie factory)].
# [ 가 )로 닫히고 있음 → "no"
# 출력: no

# 입력: ([ (([( [ ] ) ( ) (( ))] )) ]).
# 모든 괄호가 올바르게 짝을 이룸 → "yes"
# 출력: yes

# 입력: .
# 괄호가 하나도 없으므로 "yes"
# 출력: yes

#아이디어 추출
# 스택 활용 (LIFO 원칙 적용):
# 	1) 여는 괄호 ( 또는 [가 나오면 스택에 push
# 	2) 닫는 괄호 ) 또는 ]가 나오면 스택에서 pop하여 매칭 확인
# 	3) 스택이 비어 있거나 매칭이 맞지 않으면 "no"
# 올바른 매칭 확인:
#   1) (는 )로만 닫혀야 함
# 	2) [는 ]로만 닫혀야 함
# 	3) 서로 다른 괄호가 짝을 이루면 "no"
# 검사 종료 후 스택 확인:
# 	1) 모든 문자를 검사한 후 스택이 비어 있어야 "yes"
# 	2) 스택에 남은 괄호가 있다면 "no"
 
#아이디어를 문제에 적용
# 1) 문자열을 한 줄씩 읽어 처리하며, 마지막 입력 .(온점)일 경우 종료
# 2) 문자열을 순회하면서 괄호만 검사하고 나머지 문자(알파벳, 공백 등)는 무시
# 3) 스택을 활용하여 괄호를 저장하고, 올바른 괄호 짝을 맞추는지 검증
# 4) 문자열의 모든 검사가 끝난 후, 스택이 비어 있으면 "yes", 그렇지 않으면 "no" 출력
 
 
import sys

input = sys.stdin.read  # 입력을 한 번에 읽어들임 (빠른 입출력)
lines = input().splitlines()  # 줄 단위로 나누어 리스트로 저장

for line in lines:
    if line == ".":  # 종료 조건 ('.'만 입력되면 종료)
        break
    
    stack = []  # 스택 초기화 (괄호 저장)
    balanced = True  # 균형 여부를 확인하는 변수

    for char in line:  # 문자열의 모든 문자 순회
        if char in "([":  # 1) 여는 괄호는 스택에 추가
            stack.append(char)
        elif char in ")]":  # 2) 닫는 괄호 처리
            if not stack or (char == ")" and stack[-1] != "(") or (char == "]" and stack[-1] != "["):
                balanced = False  # 스택이 비어있거나 짝이 맞지 않으면 균형 깨짐
                break
            stack.pop()  # 짝이 맞는 경우 스택에서 제거

    # 3) 최종 결과 출력: 
    #   - 스택이 비어있고, 모든 괄호가 균형을 이루면 "yes"
    #   - 그렇지 않으면 "no"
    print("yes" if balanced and not stack else "no")  