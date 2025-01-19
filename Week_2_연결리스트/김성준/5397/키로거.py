# 1. 문제 이해
# 	목표: 주어진 키로거 기록을 기반으로 최종 비밀번호를 계산
# 	입력과 동작:
# 	1) 문자열은 최대 1,000,000자까지 입력 가능
# 	2) 커서의 위치는 문자열 맨 앞, 맨 뒤, 또는 중간에 위치할 수 있음
# 	3) 입력된 키는 다음 규칙에 따라 동작:
# 	    '-': 커서 왼쪽의 문자를 삭제 (맨 앞이면 무시)
# 	    '<': 커서를 왼쪽으로 이동 (맨 앞이면 무시)
# 		'>': 커서를 오른쪽으로 이동 (맨 뒤이면 무시)
# 	    알파벳/숫자: 커서 위치에 해당 문자를 삽입
# 	4)	초기 조건: 커서는 문자열의 맨 뒤에 위치
# 	5)	출력값: 모든 키 입력 처리 후의 최종 문자열
 
 
#  2. 예제 이해

# 입력
# <<BP<A>>Cd-
# ThIsIsS3Cr3t

# 출력
# BAPC
# ThIsIsS3Cr3t

# 첫 번째 테스트
# 	<<BP<A>>Cd-
# 	명령어 처리 과정:
# 	    1) <<: 커서를 두 번 왼쪽으로 이동 (변화 없음)
# 	    2) BP: B, P 삽입 → BP|
# 	    3) <A>: <로 커서 왼쪽 이동 후, A 삽입 → BAP|
# 	    4) >>: 커서를 오른쪽으로 두 번 이동 (맨 뒤) → BAP|
# 	    5) Cd: C, d 삽입 → BAPCd|
# 	    6)-: 백스페이스 → BAPC

# 결과: BAPC

# 두 번째 테스트
# 	초기: ThIsIsS3Cr3t
# 	명령어 처리: 모든 문자를 순서대로 삽입 (커서 이동 없음)

# 결과: ThIsIsS3Cr3t


# 3. 아이디어 추출
# 	1.효율적인 커서 구현:
# 	    커서 이동과 삽입/삭제를 효율적으로 처리하려면 리스트 두 개(left, right)를 활용
# 	    left: 커서 왼쪽의 문자들
# 	    right: 커서 오른쪽의 문자들
# 	2.입력 처리:
# 	    각 문자에 따라 동작:
# 	        1)	'-': left의 마지막 문자 삭제
# 	        2)	'<': left의 마지막 문자를 right로 이동
# 	        3)	'>': right의 첫 문자를 left로 이동
# 	        4)	알파벳/숫자: left에 삽입
#   3. 최종 결과 생성:
# 	    left + right[::-1]를 합쳐 결과 문자열 생성
# 	4.	효율성:
# 	    1) **O(L)**로 처리 가능 (L은 문자열 길이)
# 	    2) 리스트의 pop, append는 O(1)
 
#  4. 문제에 아이디어 접목
# 	 1.	데이터 구조 선택:
# 	    커서를 중심으로 **왼쪽 리스트(left)**와 **오른쪽 리스트(right)**를 사용해 문자열을 관리
# 	    두 리스트는 Python의 **deque**로 구현해 삽입, 삭제, 이동 연산을 O(1)에 처리
# 	 2.	명령어 처리:
# 	    입력 문자열을 한 문자씩 순회하면서 명령어에 따라 왼쪽, 오른쪽 리스트를 수정
# 	    < 명령어: 왼쪽 리스트의 마지막 문자를 오른쪽 리스트의 맨 앞에 이동
# 	    > 명령어: 오른쪽 리스트의 맨 앞 문자를 왼쪽 리스트의 마지막에 이동
# 	    - 명령어: 왼쪽 리스트의 마지막 문자를 삭제
# 	    알파벳/숫자: 왼쪽 리스트에 삽입
# 	 3.	최종 문자열 생성:
# 	    모든 명령어를 처리한 후, left와 right 리스트를 병합해 결과 문자열을 생성
# 	    오른쪽 리스트는 역순(right[::-1])으로 추가
# 	 4.	효율성 보장:
# 	    명령어 처리와 문자열 생성 모두 O(L)에 처리 가능
# 	    여러 테스트 케이스(T)에 대해 총 O(T * L) 시간 복잡도


from collections import deque
import sys

def solve():
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])  # 테스트 케이스 개수
    results = []

    for i in range(1, T + 1):
        keylog = data[i]
        left = deque()  # 커서 왼쪽 문자 저장
        right = deque()  # 커서 오른쪽 문자 저장

        for char in keylog:
            if char == '<':  # 커서를 왼쪽으로 이동
                if left:
                    right.appendleft(left.pop())
            elif char == '>':  # 커서를 오른쪽으로 이동
                if right:
                    left.append(right.popleft())
            elif char == '-':  # 백스페이스
                if left:
                    left.pop()
            else:  # 알파벳/숫자 입력
                left.append(char)

        # 결과 저장 (left + right 병합)
        results.append(''.join(left) + ''.join(right))

    # 최종 결과 출력
    sys.stdout.write('\n'.join(results) + '\n')