import math

room_number = input() 

# 크기 10인 리스트로 0 ~ 9 등장 횟수 저장
counts = [0] * 10

# 각 자릿수를 문자열로 바꾼 후 변환해서 0 ~ 9 등장 횟수 세기
for digit in room_number:
    counts[int(digit)] += 1

# 숫자 6과 9를 합쳐서 올림 처리
counts[6] = math.ceil((counts[6] + counts[9]) / 2)
counts[9] = 0  # 숫자 9는 처리 완료했으므로 초기화

# 필요한 최댓값 수
answer = max(counts)

print(answer)
