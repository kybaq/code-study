import sys

N = int(sys.stdin.readline())  # 점 개수 입력
points = []  # 좌표 저장할 리스트

# 좌표 입력받아 리스트에 추가
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x, y])  # 리스트로 저장

# 정렬: x 기준, x가 같으면 y 기준 정렬
points.sort()

for p in points:
    print(p[0], p[1])
