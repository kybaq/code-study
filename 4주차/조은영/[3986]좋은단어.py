import sys

N = int(sys.stdin.readline().strip())

good_word_count = 0

for _ in range(N):
    word = sys.stdin.readline().strip()  # 사용자에게 단어 입력
    stack = []
    
    # 단어의 각 문자 처리
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()  # 같은 글자가 있으면 제거
        else:
            stack.append(char)  # 없으면 추가
    
    # 스택이 비어있으면 좋은 단어
    if not stack:
        good_word_count += 1

print(good_word_count)
