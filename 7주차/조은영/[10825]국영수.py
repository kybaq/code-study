import sys

N = int(sys.stdin.readline().strip())  # 학생 수
students = [sys.stdin.readline().split() for _ in range(N)]  # 학생 정보 리스트

# 정수형 변환 (국어, 영어, 수학 점수를 숫자로 변환)
for student in students:
    student[1:] = map(int, student[1:])  # 점수를 정수형으로 변환

# 정렬 수행
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
