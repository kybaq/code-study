def power_mod(a, b, c):
    if b == 1:
        return a % c  # 기본 케이스: A^1 % C

    half = power_mod(a, b // 2, c)  # A^(B//2) % C 계산
    half = (half * half) % c  # 제곱하여 결과 도출

    if b % 2 == 0:
        return half  # B가 짝수인 경우
    else:
        return (half * (a % c)) % c  # B가 홀수인 경우, 추가 곱셈

A, B, C = map(int, input().split())

print(power_mod(A, B, C))
