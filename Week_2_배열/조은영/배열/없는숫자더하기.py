def solution(numbers):
    # 0 ~ 9까지 다 더한 값
    total_sum = 45
    
    # numbers의 합
    nums_sum = sum(numbers)
    
    # 결과 = 전체 - numbers의 합
    return total_sum - nums_sum


    # def solution_set(numbers):
    # {0~9}만들기
    # total = set(range(10))
    # {있는애들}
    # now = set(numbers)
    
    # missing = total - now

    # 더해서 반환
    # return sum(missing)


