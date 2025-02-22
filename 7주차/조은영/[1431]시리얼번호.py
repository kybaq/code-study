import sys

# 숫자의 합을 구하는 함수
def sum_of_digits(serial):
    return sum(int(c) for c in serial if c.isdigit())

# 입력 받기
N = int(sys.stdin.readline().strip())  # 기타 개수
serials = [sys.stdin.readline().strip() for _ in range(N)]  # 시리얼 번호 리스트

# 정렬 수행
# 우선순위 - 길이 -> 숫자 합 -> 사전
serials.sort(key=lambda x: (len(x), sum_of_digits(x), x))

for serial in serials:
    print(serial)
