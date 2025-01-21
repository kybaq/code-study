def solution(progresses, speeds):
    # 각 작업의 남은 작업 일수를 계산
    days = []

    for i in range(len(progresses)):
        # 남은 작업량 계산: 100%에서 현재 진행도를 뺀 값
        remaining_work = 100 - progresses[i]
        # 남은 일수 계산 (아래에서 올림하기 위해 -1)
        required_days = (remaining_work + speeds[i] - 1) // speeds[i]
        days.append(required_days)

    # 작업의 배포 일정을 계산
    result = []
    max_day = days[0]  # 첫 번째 작업의 완료 예정일 -> 기준
    count = 0  # 그 배포에 몇 개 포함될 지

    for day in days:
        if day <= max_day:  
            # 현재 작업의 완료 예정일이 기준일(max_day)보다 작거나 같다면
            # 같은 배포 그룹에 포함 가능하므로 count를 증가
            count += 1
        else:
            # 기준일보다 늦게 완료되는 작업이 나오면
            result.append(count)  # 지금까지의 count 값을 result에 추가
            max_day = day  # 새로운 기준일로 갱신
            count = 1  # 새로운 배포 그룹의 첫 작업이므로 count를 1로 초기화
    
    result.append(count)
    return result
