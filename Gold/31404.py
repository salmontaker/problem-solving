import sys

input = sys.stdin.readline

H, W = map(int, input().split())
R, C, D = map(int, input().split())
A = [[*map(int, [*input().strip()])] for _ in range(H)]
B = [[*map(int, [*input().strip()])] for _ in range(H)]

ROOM = [[1] * W for _ in range(H)]
VISIT = [[[0] * 4 for _ in range(W)] for _ in range(H)]
DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans, cnt = 0, 0

while True:
    VISIT[R][C][D] = 1
    # 작동 횟수. (이동을 해야만 증가하는게 아님에 유의.)
    cnt += 1

    if ROOM[R][C] == 1:
        ROOM[R][C] = 0
        D = (D + A[R][C]) % 4

        # 먼지 청소시, 경로가 달라질 수 있으므로 방문배열 초기화
        VISIT = [[[0] * 4 for _ in range(W)] for _ in range(H)]
        # 시뮬레이션 속의 청소기가 마지막으로 청소한 시점이 정답.
        ans = cnt
    else:
        D = (D + B[R][C]) % 4

    R, C = R + DELTA[D][0], C + DELTA[D][1]

    if not (-1 < R < H and -1 < C < W):
        break

    if VISIT[R][C][D]:
        break

print(ans)
