def hanoi(n, start, end, mid, result):
    if n == 1:
        result.append(f"{start} {end}")
        return
    hanoi(n - 1, start, mid, end, result)  # N-1개를 보조 장대로 이동
    result.append(f"{start} {end}")        # 가장 큰 원판을 목표 장대로 이동
    hanoi(n - 1, mid, end, start, result)  # N-1개를 목표 장대로 이동

# 입력 받기
N = int(input())

# 이동 경로 저장 리스트
result = []
hanoi(N, 1, 3, 2, result)

print(len(result))  # 총 이동 횟수
print("\n".join(result))  # 이동 과정
