import sys

N = int(sys.stdin.readline().strip())
members = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), i, name))  # 가입 순서 i를 추가하여 안정 정렬 유지

# 정렬: 나이 기준으로 정렬 (가입 순서는 자동으로 유지됨)
members.sort()

for age, _, name in members:
    print(age, name)
