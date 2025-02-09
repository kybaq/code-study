#문제 이해
# A를 B번 곱한 후 C로 나눈 나머지를 구해야됨
# 재귀를 활용한 분할 정복 방식으로 빠르게 해결해야됨
 
#예제 이해

# 입력: 10 11 12

# 계산 과정: (10^11) % 12 =>  4

# 출력: 4

#아이디어 추출 (재귀 활용)
# 거듭제곱을 절반으로 나누어 계산
# 	1) B가 짝수이면 → (A^(B/2))^2 % C
# 	2) B가 홀수이면 → (A^(B//2))^2 * A % C
# 재귀적으로 계산
# 	1) B == 1이면, A % C 반환 (기본 종료 조건)
# 	2) B를 절반으로 줄이며 계산 → O(log B) 시간 복잡도
# 모듈러 연산 활용
# 	1) (X * Y) % C = ((X % C) * (Y % C)) % C
# 	2) 중간 계산에서 나머지를 계속 취해 큰 수 연산을 방지
 
#아이디어를 문제에 적용
# 기본 종료 조건
#   1) B == 1이면 A % C를 반환하여 재귀 종료
# 거듭제곱을 절반으로 나눠서 재귀 호출
# 	1) B를 B // 2로 줄여서 재귀적으로 계산
# 	2) 이를 통해 연산 횟수를 O(log B)로 줄임
# 짝수/홀수 처리
# 	1) B가 짝수: (A^(B/2))^2 % C
# 	2) B가 홀수: (A^(B//2))^2 * A % C
# 모듈러 연산 활용
# 	1) 중간 계산마다 % C를 적용하여 큰 수 연산 방지
# 최종 결과 반환
# 	1) B == 1까지 재귀적으로 줄이며 값을 반환

 
import sys

def modular_exponentiation(base, exp, mod):
    
    # 기본 종료 조건: B가 1이면 A % C 반환
    if exp == 1:
        return base % mod
    
    # 지수를 절반으로 줄여서 재귀 호출
    half_mod = modular_exponentiation(base, exp // 2, mod)
    
    # 짝수/홀수에 따라 결과 계산
    if exp % 2 == 0:
        return (half_mod * half_mod) % mod  # 짝수일 때: (half^2) % mod
    else:
        return (half_mod * half_mod * base) % mod  # 홀수일 때: (half^2 * base) % mod

# 입력 처리
A, B, C = map(int, sys.stdin.readline().split())

# 결과 출력 (모듈러 연산 적용)
print(modular_exponentiation(A, B, C))