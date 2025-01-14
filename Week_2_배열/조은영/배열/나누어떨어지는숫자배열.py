def solution(arr, divisor):

    # 정답 담을 리스트
    answer = []
    
    # arr의 모든 원소에 대해 divisor로 나눠떨어지는지 보고 뒤에 붙임
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    
    # 없으면 [-1] 리턴
    if not answer:
        return [-1]
    
    # 나누어 떨어지는 원소 있으면 오름차순 정렬 후 반환
    answer.sort()
    return answer
