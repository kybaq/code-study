def solution(participant, completion):
    # 두 리스트 모두 오름차순 정렬
    participant.sort()
    completion.sort()
    
    # 참가자 리스트와 완주자 리스트를 인덱스로 비교
    for i in range(len(completion)):
        # i번째 참가자와 i번째 완주자의 이름이 다르면, 바로 그 참가자가 완주 못한 사람
        if participant[i] != completion[i]:
            return participant[i]
    
    # 끝까지 다른 사람을 못 찾았다면 결국 마지막 사람
    return participant[-1]
