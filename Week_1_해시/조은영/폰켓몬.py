def solution(nums):
    # 전체 폰켓몬 수
    total_mon = len(nums)
    
    # 중복 상관없이 리터럴리 폰켓몬 종류의 수
    distinct_mon = len(set(nums))
    
    # 가져갈 수 있는 폰켓몬의 총 수(N/2)
    pick_mon = total_mon / 2
    
    # "가질 수 있는 폰켓몬 종류의 최대 개수" = 
    # (중복 없이 종류의 개수)와 (가져갈 수 있는 마리 수) 중 작은 값
    return min(distinct_mon, pick_mon)
