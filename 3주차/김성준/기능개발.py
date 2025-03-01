#1.문제 이해
# 작업 진도와 속도가 주어질 때 각 배포마다 몇개의 기능이 배포되는지 계산하기


#2.예제 이해
# 예제1
# 	입력: progresses = [93, 30, 55] , speeds = [1, 30, 5]
# 	처리 과정:
#    1. 각 작업이 완료되기까지 남은 일수:
# 		1) 첫 번째 작업: (100 - 93) // 1 = 7일
# 		2) 두 번째 작업: (100 - 30) // 30 = 3일
# 		3) 세 번째 작업: (100 - 55) // 5 = 9일
#    2.	배포:
#       1)	7일째: 첫 번째와 두 번째 작업 배포 → [2, ...]
#       2)	9일째: 세 번째 작업 배포 → [2, 1]
#   출력: [2, 1]

# 예제2
# 	입력: 입력: progresses = [95, 90, 99, 99, 80, 99] , speeds = [1, 1, 1, 1, 1, 1]
# 	처리 과정:
#    1. 각 작업이 완료되기까지 남은 일수:
# 		1) [5, 10, 1, 1, 20, 1]
#    2.	배포:
#       1)	5일째: 첫 번째 작업 → [1, ...]
#       2)	10일째: 두 번째, 세 번째, 네 번째 작업 → [1, 3, ...]
#       3)  20일째: 다섯 번째와 여섯 번째 작업 → [1, 3, 2]
#   출력: [1, 3, 2]

#3.아이디어 정리
# 1. 남은 작업일 계산:
#   1)	각 작업에 대해 (100 - progress) // speed로 작업 완료에 필요한 남은 일수를 계산
# 	2)	소수점이 생기는 경우를 대비해 ceil을 사용해 올림
# 2. 배포 그룹화:
#   1) 순차적으로 작업을 확인하면서 앞의 작업이 끝난 날보다 더 오래 걸리는 작업이 나오면 새로운 배포일로 그룹화
# 3. 효율성 고려:
#   작업이 순차적으로 처리되므로, 한 번의 순회로 문제를 해결 가능함 그래서 O(n)을 사용

#4.아이디어를 문제에 적용
# 1) 각 작업의 남은 작업일을 계산
# 2) 첫 번째 작업의 완료일을 기준으로 그룹화
# 3) 새로운 작업일이 더 길어지면 새로운 배포 그룹으로 이동

from math import ceil

def solution(progresses, speeds):
    # 1. 각 작업의 남은 작업일을 계산
    # (100 - progress) / speed를 올림하여 완료까지 필요한 일수를 계산
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    # 결과를 저장할 리스트
    result = []
    # 첫 번째 작업의 완료일을 기준으로 그룹화 시작
    current_day = days[0]  # 첫 번째 작업의 완료일
    count = 0  # 현재 그룹의 작업 개수

    for day in days:
        # 2. 새로운 작업일이 더 길어지면 새로운 배포 그룹으로 이동
        if day > current_day:
            result.append(count)  # 이전 배포 그룹의 작업 개수 저장
            current_day = day  # 현재 기준 작업 완료일 갱신
            count = 1  # 새로운 그룹 시작
        else:
            count += 1  # 기존 그룹에 작업 추가

    result.append(count)
    return result