#문제 이해

# 이 문제는 학생 N명의 이름과 국어, 영어, 수학 점수가 주어질 때, 특정한 정렬 기준을 적용하여 학생의 이름을 출력하는 문제

# 정렬 기준은 다음과 같다:
# 	1.	국어 점수 감소 순서 (내림차순)
# 	2.	국어 점수가 같으면 영어 점수 증가 순서 (오름차순)
# 	3.	국어와 영어 점수가 같으면 수학 점수 감소 순서 (내림차순)
# 	4.	모든 점수가 같으면 이름을 사전 순으로 증가하는 순서 (오름차순, 대소문자 구분 O)
# 즉, 주어진 데이터를 정렬 기준에 맞춰 정렬하고, 학생 이름만 출력하는 문제다.

#예제 이해

# 입력
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# 정렬 과정
# 	1.	국어 점수 내림차순 정렬
# 80: Sangkeun, Sunyoung, Donghyuk, nsj
# 70: Sei, Wonseob, Sanghyun
# 60: Kangsoo
# 50: Junkyu, Soong, Haebin, Taewhan

# 	2.	국어 점수가 같다면 영어 점수 오름차순 정렬
# 80: Donghyuk(60), Sangkeun(60), Sunyoung(70), nsj(80)
# 70: Sei(70), Wonseob(70), Sanghyun(70)
# 50: Junkyu(60), Soong(60), Haebin(60), Taewhan(60)

# 	3.	국어, 영어 점수가 같다면 수학 점수 내림차순 정렬
# 80: Donghyuk(60, 100), Sangkeun(60, 50), Sunyoung(70, 100), nsj(80, 80)
# 70: Sei(70, 70), Wonseob(70, 90), Sanghyun(70, 80)
# 50: Junkyu(60, 100), Haebin(60, 100), Soong(60, 90), Taewhan(60, 90)

# 	4.	모든 점수가 같으면 이름 사전순 정렬
# Donghyuk, Sangkeun, Sunyoung, nsj, Wonseob, Sanghyun, Sei, Kangsoo, Haebin, Junkyu, Soong, Taewhan

# 출력 
# Donghyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan


#아이디어 창출
# 정렬 기준을 명확하게 정의
#   1) 국어 점수는 내림차순 => -국어
# 	2) 영어 점수는 오름차순 => 영어
# 	3) 수학 점수는 내림차순 => -수학
# 	4) 이름은 사전순(오름차순) => 이름
# Python의 sort() 함수 활용
# 	1) sort()는 튜플 형태의 정렬 기준을 적용할 수 있으므로, (국어, 영어, 수학, 이름) 형태로 정렬
# 	2) sort()는 기본적으로 오름차순이므로 내림차순이 필요한 경우 -를 붙임
     
#아이디어를 문제에 적용
# 	1) sys.stdin.readline()을 사용하여 빠르게 입력을 받기
# 	2) N을 입력받고, 이후 학생들의 정보를 리스트로 저장
# 	3) map(int, students[i][1:])을 사용하여 이름을 제외한 점수를 정수형으로 변환
# 	4) sort() 함수를 사용하여 정렬 기준을 적용
#       국어 점수 내림차순
# 	    영어 점수 오름차순
# 	    수학 점수 내림차순
# 	    이름 오름차순
# 	5) 정렬된 결과에서 학생 이름만 출력

import sys

# 입력 받기
N = int(sys.stdin.readline().strip())  # 첫 줄에서 N 입력 받기
students = [sys.stdin.readline().split() for _ in range(N)]  # 학생 정보 입력받기

# 점수를 정수형으로 변환
for i in range(N):
    students[i][1:] = map(int, students[i][1:])  # 이름을 제외한 점수를 정수형으로 변환

# 정렬 (정렬 기준: 국어 오름, 영어 내림, 수학 내림, 이름: 오름)
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름만 출력
for student in students:
    print(student[0])