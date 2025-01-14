# 잘라낼 때 완전히 새로운 리스트를 매번 만들지 않고 인덱스 범위를 조절해서 확인
def solution(arr, query):

    # first와 last는 arr 중 남아 있는 구간
    first, last = 0, len(arr) - 1

    for i in range(len(query)):
        # 현재 query[i] 현재 남아있는 배열, 조절한 인덱스
        # 전체 arr 기준으로는 first + query[i]가 실제 인덱스임 이거 놓쳐서 시간 더 씀
        cut_index = first + query[i]

        if i % 2 == 0:  
            # 짝수 번째 쿼리면 뒷부분 잘라내서 버리기
            # 즉, last cut_index로 조정
            last = cut_index
        else:
            # 홀수 번째 쿼리면 앞부분 잘라내서 버리기
            # 즉, first cut_index로 조정
            first = cut_index

    # 모든 쿼리 처리 후, arr[first : last+1] 반환
    return arr[first : last+1]