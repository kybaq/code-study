from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 큐를 사용하여 다리를 표현
    bridge = deque([0] * bridge_length)  # 다리의 길이만큼 0으로 초기화
    total_weight = 0
    time = 0
    truck_weights = deque(truck_weights)  # 대기 트럭 리스트를 큐로 변환

    while bridge:
        # 시간이 1초씩 흐름
        time += 1

        # 다리에서 트럭 내려가기
        left_truck = bridge.popleft()  # 다리의 맨 앞 트럭이 나감
        total_weight -= left_truck  # 나간 트럭의 무게를 총 무게에서 빼줌

        # 대기 트럭이 있으면 다리에 올릴지 판단
        if truck_weights:
            # 대기 트럭의 무게와 현재 다리 위의 무게 합이 ㄱㅊ으면 트럭 추가
            if total_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()  # 대기 트럭 중 첫 번째 트럭을 꺼냄
                bridge.append(next_truck)  # 다리의 끝에 트럭 추가
                total_weight += next_truck  # 다리 위 총 무게 갱신
            else:
                # 다리가 무게를 견딜 수 없으면 0을 추가
                bridge.append(0)

    return time
