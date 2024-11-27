def can_travel(N, visits):
    current_x, current_y, current_time = 0, 0, 0

    for i in range(N):
        t_i, x_i, y_i = visits[i]
        
        # 移動に必要な時間と移動すべき距離を計算
        time_diff = t_i - current_time
        distance = abs(x_i - current_x) + abs(y_i - current_y)

        # 到達可能かをチェック
        if distance > time_diff or (time_diff - distance) % 2 != 0:
            return "No"

        # 状態を更新
        current_x, current_y, current_time = x_i, y_i, t_i

    return "Yes"

# 入力の読み込み
N = int(input())
visits = [tuple(map(int, input().split())) for _ in range(N)]

# 判定して出力
result = can_travel(N, visits)
print(result)
