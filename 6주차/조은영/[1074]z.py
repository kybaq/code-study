def z_search(n, r, c):
    if n == 0:
        return 0  # 1x1 배열의 경우 항상 0번째 방문

    size = 2 ** (n - 1)  # 현재 배열의 한 변 크기 (절반 크기)
    area_size = size * size  # 한 사분면의 크기

    if r < size and c < size:  # 왼쪽 위 (0번 영역)
        return z_search(n - 1, r, c)
    elif r < size and c >= size:  # 오른쪽 위 (1번 영역)
        return area_size + z_search(n - 1, r, c - size)
    elif r >= size and c < size:  # 왼쪽 아래 (2번 영역)
        return 2 * area_size + z_search(n - 1, r - size, c)
    else:  # 오른쪽 아래 (3번 영역)
        return 3 * area_size + z_search(n - 1, r - size, c - size)

N, r, c = map(int, input().split())

print(z_search(N, r, c))
