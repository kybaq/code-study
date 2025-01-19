def solution(arr):
    result = []  # 결과를 저장할 리스트
    
    # arr 배열 숫자를 하나씩 꺼내서 num에 저장하며 반복
    for num in arr:
        # 아직 숫자 추가 안됐거나 마지막 요소와 현재 요소가 다를 경우
        if not result or result[-1] != num:
            # result에 num 추가
            result.append(num)
    
    return result
