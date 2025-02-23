#문제 이해
# 주어진 N개의 정수를 오름차순으로 정렬하는 문제
# 수는 중복되지 않음
# 결과는 정렬된 숫자를 한 줄씩 출력하는 형태

#예제 이해
# 입력:
# 5
# 5
# 2
# 3
# 4
# 1

# 출력:

# 1
# 2
# 3
# 4
# 5

# 패턴 분석
# 입력된 숫자들을 리스트에 저장하고 정렬하면 쉽게 해결 가능
# 중복이 없으므로 정렬만 수행하면 됨 (중복 제거 과정 필요 없음)
# 숫자의 범위가 절댓값 1,000 이하이므로, 일반적인 정렬 알고리즘을 사용해도 빠르게 처리 가능

#아이디어 창출
# 1) 입력값을 리스트로 저장
# 2) 파이썬 내장 정렬 함수를 활용하여 오름차순 정렬 수행 (Timsort 기반으로 빠름)
# 3) 정렬된 리스트의 각 값을 한 줄씩 출력
# 4) 시간 복잡도 고려 → O(N log N) 정도의 정렬 알고리즘이면 충분히 해결 가능

#아이디어를 문제에 적용
# 1) N을 입력받음
# 2) N개의 정수를 리스트에 저장
# 3) 리스트를 오름차순 정렬 (내장 정렬 함수 사용)
# 4) 정렬된 리스트의 각 값을 출력

import sys

# 입력 받기
N = int(sys.stdin.readline().strip())  # 첫 번째 줄: 정수 개수
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]  # N개의 정수 입력

# 정렬 수행
numbers.sort()

for num in numbers:
    print(num)