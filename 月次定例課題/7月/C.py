def find_integer_sequence(N, ranges):
    X = []
    total_min_sum = 0
    total_max_sum = 0
    
    # 各範囲の最小値を使って初期化し、合計を計算
    for L, R in ranges:
        total_min_sum += L
        total_max_sum += R
        X.append(L)
    
    # 最小合計が0以下、最大合計が0以上でなければNo
    if total_min_sum > 0 or total_max_sum < 0:
        print("No")
        return
    
    remaining_sum = -total_min_sum
    for i in range(N):
        L, R = ranges[i]
        current_val = X[i]
        available_increment = R - current_val
        if remaining_sum > 0:
            increment = min(available_increment, remaining_sum)
            X[i] += increment
            remaining_sum -= increment

    print("Yes")
    print(" ".join(map(str, X)))

# 標準入力からデータを受け取る
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
ranges = []
index = 1
for _ in range(N):
    L = int(data[index])
    R = int(data[index + 1])
    ranges.append((L, R))
    index += 2

find_integer_sequence(N, ranges)
