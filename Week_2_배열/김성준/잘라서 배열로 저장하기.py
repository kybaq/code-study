# 1. 문제 이해
# 	목표: 문자열 my_str을 길이 n씩 잘라 배열로 반환
# 	제약 조건:
# 	1.	문자열의 길이가 n으로 나누어떨어지지 않으면 마지막 조각은 남은 문자열만 포함
# 	2.	문자열은 알파벳 대소문자와 숫자로 구성
# 	3.	반환값은 배열이어야 함

# 2. 예제 분석

# 1).
# 	입력값: my_str = "abc1Addfggg4556b", n = 6
# 	출력값: ["abc1Ad", "dfggg4", "556b"]
# 2)
# 	입력값: my_str = "abcdef123", n = 3
# 	출력값: ["abc", "def", "123"]

 
# 3. 아이디어
# 	1.슬라이싱을 이용한 조각 만들기:
# 	    1) 문자열의 특정 구간을 자르기 위해 슬라이싱 사용
# 	    2) my_str[start:end]로 자르면 원하는 부분을 쉽게 추출 가능
# 	2.반복문을 사용해 문자열을 나누기:
# 	    1) 문자열의 길이를 기준으로, 시작 인덱스를 0부터 n씩 증가
# 	    2) range(0, len(my_str), n)을 활용.
# 	3.결과 배열에 추가:
# 	    1) 잘라낸 문자열을 배열에 하나씩 추가
# 	4.결과 반환:
# 	    1) 모든 조각을 저장한 배열을 반환

# https://school.programmers.co.kr/learn/courses/30/lessons/120913?language=python3

def solution(my_str, n):
    answer = [] # 결과 배열을 초기화
    
    for i in range(0, len(my_str), n): # i는 0부터 n씩 증가
        answer.append(my_str[i:i+n]) # my_str[i:i+n]으로 i번째부터 n개의 문자를 추출, append()로 answer에 추가
        
    return answer