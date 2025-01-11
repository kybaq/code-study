# 1. 문제이해
#   마라톤 참여한 선수 리스트 : participant
#   마라톤 완주한 선수 리스트 : completion
#   동명이인이 있을 수 있다.
#   completion길이는 participant의 길이보다 1작다.
#   return: 완주하지 못한 단 한 명의 선수의 이름

# 2. 예제이해
#   participant = ["leo", "kiki", "eden"]
#   completion =  [       "kiki", "eden"]
# return: ["leo"]

#   participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
#   completion =  ["josipa", "filipa", "marina", "nikola"]
# return: ["vinko"]

# 3. 아이디어 접목
#   1). participant에는 있지만, completion에는 없는 이름을 찾아야 함
#   2). 단, 동명이인이 있으므로 중복 횟수까지 고려해야 함
#   3). 두 리스트를 정렬한 뒤, 순서대로 비교
#   4). participant와 completion과 짝을 지어 묶었을때 짝이 없는 사람이 완주하지 못한 사람이다

# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    
    # 두 리스트를 정렬
    participant.sort() # 기본적으로 오름차순으로 정렬됨
    completion.sort()
    
    # 정렬된 리스트를 순차적으로 비교
    for p, c in zip(participant, completion):
        if p != c: # 만약 서로 다르다면 완주하지 못한 사람임
            return p # 참여만하고 완주하지 못한 사람
        
    return participant[-1]  # participant 리스트의 마지막 요소를 반환 (완주하지 못한 사람)