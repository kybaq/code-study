#문제 이해
# 주어진 단어 begin을 target으로 변환하는 최소 과정을 찾는 문제
# 규칙:
#   1) 한 번에 한 개의 알파벳만 변경 가능
# 	2) 변경된 단어는 반드시 words 리스트에 존재해야 함
# 변환이 불가능하면 0을 반환
 
#예제 이해
# 예제 1:
# begin = "hit", target = "cog", words = ["hot","dot","dog","lot","log","cog"]
# 변환 과정:
# 	1)	"hit" → "hot"
# 	2)	"hot" → "dot"
# 	3)	"dot" → "dog"
# 	4)	"dog" → "cog" (최종 도착)
# 최소 단계 수: 4

# 예제 2:
# begin = "hit", target = "cog", words = ["hot", "dot", "dog", "lot", "log"]
# "cog"가 words 리스트에 없으므로 변환 불가 → 결과: 0
 
#아이디어 추출
# 	그래프 탐색 방식으로 접근 가능
# DFS를 활용하여 탐색:
# 	1) begin 단어에서 시작하여 words 리스트에 있는 단어 중 한 개의 문자만 다른 단어로 이동
# 	2) 방문한 단어는 다시 방문하지 않음 (중복 방지)
# 	3) target에 도착하면 변환 횟수를 반환
# 	4) 모든 경우를 탐색하여 최소 변환 횟수를 찾음
 
#아이디어를 문제에 적용
# DFS를 사용하여 begin에서 target으로 가는 모든 가능한 경로를 탐색
# 변환 조건:
# 	1) 한 개의 문자만 다른 단어로 이동
# 	2) words 리스트에 있는 단어로만 이동 가능
# DFS 종료 조건:
# 	1) target 단어에 도달하면 변환 횟수를 반환
# 	2) words에 더 이상 변환할 단어가 없으면 종료
 
from collections import deque

def is_single_letter_different(word1, word2):
    """두 단어가 단 하나의 문자만 다를 경우 True 반환"""
    return sum(1 for a, b in zip(word1, word2) if a != b) == 1

def find_min_transformations(current_word, target_word, word_list, visited, steps):
    """DFS 탐색을 통해 최소 변환 횟수 찾기"""
    if current_word == target_word:  # 목표 단어에 도달하면 변환 횟수 반환
        return steps

    min_steps = float('inf')  # 최소 변환 횟수 저장

    for idx, next_word in enumerate(word_list):
        if not visited[idx] and is_single_letter_different(current_word, next_word):
            visited[idx] = True  # 방문 체크
            result = find_min_transformations(next_word, target_word, word_list, visited, steps + 1)
            if result is not None:
                min_steps = min(min_steps, result)
            visited[idx] = False  # 백트래킹

    return min_steps if min_steps != float('inf') else None

def solution(begin, target, words):
    if target not in words:  # 변환할 수 없는 경우
        return 0

    visited = [False] * len(words)  # 방문 여부 체크 배열
    result = find_min_transformations(begin, target, words, visited, 0)

    return result if result is not None else 0