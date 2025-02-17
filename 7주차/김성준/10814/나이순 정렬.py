#문제 이해
# 회원들의 나이와 이름이 주어지고, 이를 특정 조건에 맞게 정렬하는 문제
# 나이를 기준으로 오름차순 정렬하되, 나이가 같으면 가입 순서를 유지해야 함


#예제 이해
# 입력:
# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

# 오름차순 정렬하면:
# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun
# 나이를 기준으로 정렬하되, 같은 나이면 원래 입력 순서를 유지해야 함
# 즉, Python의 정렬 알고리즘에서 안정 정렬(Stable Sort)이 필요함
# 기본 정렬 함수 `sorted()`나 `sort()`는 Timsort(O(N log N))로 안정 정렬을 보장하므로 사용 가능

## 아이디어 창출
# 1) 입력을 리스트에 저장 (튜플 형태: (나이, 이름))
# 2) 나이를 기준으로 정렬 (같은 나이면 원래 입력 순서 유지)
# 3) `sorted()` 또는 `.sort()`를 사용해 안정 정렬 수행
# 4) 정렬된 리스트를 출력

## 4. 아이디어를 문제에 적용
# 1) `N`을 입력받음
# 2) `N`개의 (나이, 이름) 데이터를 리스트에 저장
# 3) 리스트를 **나이를 기준으로 오름차순 정렬** (Stable Sort 보장)
# 4) 정렬된 리스트를 한 줄씩 출력


import sys

# 입력 받기
N = int(sys.stdin.readline().strip())  # 첫 번째 줄: 회원 수
members = [tuple(sys.stdin.readline().split()) for _ in range(N)]  # (나이, 이름) 형태로 저장

# 나이를 정수형으로 변환
members = [(int(age), name) for age, name in members]

# 정렬 수행 (Stable Sort 보장)
members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)