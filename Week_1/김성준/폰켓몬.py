# 1. 문제이해
#   총 N마리 폰켓몬 중에서 N/2마리를 선택해야 함
#   선택한 폰켓몬의 종류가 최대한 다양해야 함
#   return: 선택한 폰켓몬의 최대 종류 수

# 2. 예제이해
#   1). nums = [3,3,3,2,2,4]
#       result = 3
#       고유한 폰켓몬의 종류 수  = 중복을 제외하면 {3, 2, 4} = 3
#       선택 가능한 최대 폰켓몬 수 (n/2) = 6/2 = 3
#   2). nums = [3,3,3,2,2,2]
#        result = 2
#       고유한 폰켓몬의 종류 수  = 중복을 제외하면 {3, 2} = 2
#       선택 가능한 최대 폰켓몬 수 (n/2) = 6/2 = 3

# 3. 아이디어 접목
#   1). 중복을 제거해야함
#   2). (n/2)의 개수를 파악
#   3). 두가지의 경우를 전부 다 고려해야 함
#   4). 두가지 경우의 수 중에 최솟값이 정답이다.

# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):

    poketmons = set(nums) # 중복 제거
    maxPoketmons = len(nums) // 2 # n/2의 개수 파악
    return min(len(poketmons), maxPoketmons) # 두가지 경우의 수 중에 최솟값을 구함



