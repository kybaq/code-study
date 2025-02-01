#문제 이해
# 주어진 단어가 “좋은 단어”인지 판별해야됨
# “좋은 단어”의 정의:
#   1) 같은 문자(A는 A, B는 B)끼리 짝을 이룰 수 있어야됨
# 	2) 쌍을 이루는 과정에서 선이 교차하면 안됨
# 	3) 즉, 문자들이 연속적으로 등장하면서 짝을 맞출 수 있어야함
# 핵심 개념: 스택(Stack) 활용
# 	1) 같은 문자가 연속으로 등장할 경우 서로 짝을 맞춰서 제거 가능해야됨
# 	2) 최종적으로 스택이 비어 있어야 “좋은 단어”
 
 
#예제 이해
# 입력:
# 3

# ABAB
# AABB
# ABBA

# 단어 분석
# ABAB => A와 B가 교차해서 짝을 맞출 수 없음 ❌ (좋은 단어 아님)
# AABB => (AA) 짝 지음 → (BB) 짝 지음 ✅ (좋은 단어)
# ABBA => (AB) 먼저 짝 지음 → (BA) 남음 → 다시 짝 지음 ✅ (좋은 단어)

# 출력:
# 2

#아이디어 추출
# 각 단어를 왼쪽부터 한 글자씩 탐색
#   1) 스택이 비어 있으면 현재 문자를 push
#   2) 스택의 최상단(top)과 현재 문자가 같다면 pop (서로 짝을 이루고 제거)
#   3) 그렇지 않으면 push
# 최종적으로 스택이 비어 있으면 “좋은 단어”
#   1) 스택이 남아 있으면 짝을 맞출 수 없는 문자가 있다는 뜻이므로 “좋은 단어”가 아님
# 전체 단어를 순회하여 좋은 단어 개수 카운트
 
#아이디어를 문제에 적용
# 문자열을 하나씩 탐색하며 스택을 활용
#   1) 현재 문자가 스택의 최상단(top)과 같다면 pop (짝을 지음)
#   2) 다르면 push (짝을 이룰 가능성이 있음)
# 검사가 끝난 후, 스택이 비어 있으면 “좋은 단어”
#   1) 비어 있으면 모든 문자들이 짝을 이루었으므로 count 증가
#   2) 스택에 문자가 남아 있다면 짝이 맞지 않으므로 “좋은 단어”가 아님
# 이 과정을 모든 단어에 반복하여 “좋은 단어”의 개수를 계산하여 출력

import sys

def count_good_words():
    num_words = int(sys.stdin.readline().strip())  # 단어 개수 입력
    valid_count = 0  # 좋은 단어 개수

    for _ in range(num_words):
        chars = sys.stdin.readline().strip()  # 단어 입력
        stack_checker = []  # 스택 역할 리스트

        # 문자열을 하나씩 확인하면서 처리
        for letter in chars:
            if stack_checker and stack_checker[-1] == letter:
                stack_checker.pop()  # 같은 문자가 연속되면 제거
            else:
                stack_checker.append(letter)  # 스택에 추가
        
        # 스택이 비어 있으면 '좋은 단어'
        if not stack_checker:
            valid_count += 1

    print(valid_count)  # 최종적으로 좋은 단어 개수 출력

count_good_words()