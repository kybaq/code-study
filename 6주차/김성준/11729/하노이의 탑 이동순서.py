# 문제 이해
# 하노이의 탑 문제는 3개의 기둥과 N개의 원판이 있을 때 첫 번째 기둥에 있는 원판들을 세 번째 기둥으로 최소 횟수로 이동하는 문제
#  이동 규칙:
# 	1) 한 번에 하나의 원판만 이동 가능
# 	2) 큰 원판 아래에 작은 원판만 놓을 수 있음
# 	3)	모든 원판을 최소 횟수로 이동해야 함
 
# 2. 예제 이해
# 입력 : 3
# 출력: 
# 7
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3

# 이해 과정
# 원판 3개를 첫 번째 기둥에서 세 번째 기둥으로 옮기려면:
# 	N=3인 경우
# 	1)  1번 원판을 1 => 3
# 	2)	2번 원판을 1 => 2
# 	3)	1번 원판을 3 => 2
# 	4)	3번 원판을 1 => 3
# 	5)	1번 원판을 2 => 1
# 	6)	2번 원판을 2 => 3
# 	7)	1번 원판을 1 => 3
# 이동 횟수 7번

#아이디어 추출
# N개의 원판을 1번 장대 => 3번 장대로 이동하는 문제를 작은 문제로 나눌 수 있음
#   기본 개념:
# 	1) N-1개의 원판을 1번 => 2번 기둥으로 이동 (보조 기둥 사용)
# 	2)	가장 큰 원판 N을 1번 => 3번 기둥으로 이동
# 	3)	N-1개의 원판을 2번 => 3번 기둥으로 이동
# 재귀적으로 작은 문제로 쪼개며 해결 가능
# 이동 횟수 공식:
# 	1) 하노이의 탑 이동 횟수는 2^N - 1
 
#아이디어를 문제에 적용
# 기본 동작:
#   1) disk_count - 1개의 원반을 from_pole → helper_pole로 이동
#   2)	가장 큰 원반을 from_pole → to_pole로 이동
#   3)	disk_count - 1개의 원반을 helper_pole → to_pole로 이동
# 최소 이동 횟수 출력:
#   1)	2^N - 1 공식 이용하여 최소 이동 횟수 계산 및 출력
# 이동 과정 출력:
#   1) print(from_pole, to_pole)를 통해 실제 원반 이동 과정을 한 줄씩 출력
 
def move_disks(disk_count, from_pole, to_pole, helper_pole):
    
    if disk_count == 1:
        print(from_pole, to_pole)
        return
    
    # 위쪽 (N-1개) 원반을 보조 기둥으로 이동
    move_disks(disk_count - 1, from_pole, helper_pole, to_pole)
    
    # 가장 큰 원반을 목표 기둥으로 이동
    print(from_pole, to_pole)
    
    # 보조 기둥에 있는 (N-1개) 원반을 목표 기둥으로 이동
    move_disks(disk_count - 1, helper_pole, to_pole, from_pole)

# 입력 받기
total_disks = int(input())  # 원반 개수 입력
print(2**total_disks - 1)  # 최소 이동 횟수 출력

# 하노이의 탑 실행
move_disks(total_disks, 1, 3, 2)