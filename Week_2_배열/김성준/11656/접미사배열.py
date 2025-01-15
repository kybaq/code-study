# 1. 문제 이해
# 	목표: 문자열 S의 모든 접미사를 구한 뒤, 이를 사전순으로 정렬하여 출력
# 	ex: 문자열 S = "baekjoon"의 접미사:
# 	    baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n
# 	출력: 접미사들을 사전순으로 정렬한 결과
 
#  2. 예제 이해
# 예제
# 	입력값: S = "baekjoon"
# 	접미사:
# 	baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n
# 	사전순 정렬:
# aekjoon
# baekjoon
# ekjoon
# joon
# kjoon
# n
# on
# oon

# 3. 아이디어 추출
# 	1)	접미사 생성:
# 	문자열 S의 각 인덱스 i에서 시작하는 부분 문자열을 구하기
# 	-> 슬라이싱을 사용
# 	2)	사전순 정렬:
# 	-> 접미사들을 리스트에 저장하고 sorted()를 사용하여 정렬
# 	3.	결과 출력:
# 	-> 정렬된 접미사 리스트의 각 요소를 출력
 
#  4. 문제에 아이디어 접목
# 	1)	문자열 S를 입력하기
# 	2)	접미사를 저장할 리스트를 생성
# 	3)	S의 각 인덱스 i에서 슬라이싱을 사용해서 접미사를 리스트에 추가
# 	4)	리스트를 sorted()로 사전순 정렬
# 	5)	정렬된 리스트를 순회하며 접미사를 출력

def suffix_array(S):
   
    suffixes = [S[i:] for i in range(len(S))]  #모든 접미사를 리스트로 생성
   
    sorted_suffixes = sorted(suffixes) #접미사를 사전순으로 정렬
    
   
    for suffix in sorted_suffixes:  #정렬된 접미사 출력
        print(suffix)

# 입력
S = input().strip()  #문자열 입력
suffix_array(S)