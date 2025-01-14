# 1.  문제이해
# 배열을 거꾸로 뒤집으면됨,,,,

# 2. 예제 분석

# 예제1        
# 1) 입력값: num_list = [1,2,3,4,5,6,7,8] 
# 2) 출력값: result =[8,7,6,5,4,3,2,1]

# 아이디어 접목

# 1) 그냥 배열 뒤집기하려면 reverse함수 쓰면 되능거 아닌가?

def solution(num_list):
    num_list.reverse()  # reverse함수를 사용해서 배열을 뒤집어봤다..
    return num_list # 정답이네..?