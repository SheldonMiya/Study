def solve(N, K, P):
    # 0-based indexingにするためPを1つずらす
    P = [p - 1 for p in P]  # 1-based to 0-based
    original_P = P[:]
    
    # 操作をK回行う（ただし周期を利用する）
    history = []
    visited = {}

    for i in range(K):
        if tuple(P) in visited:
            cycle_start = visited[tuple(P)]
            cycle_length = i - cycle_start
            remaining_operations = (K - cycle_start) % cycle_length
            for _ in range(remaining_operations):
                P = [P[p] for p in P]
            break
        visited[tuple(P)] = i
        history.append(P[:])
        P = [P[p] for p in P]

    return [p + 1 for p in P]  # 1-based indexingに戻す

# 入力の読み込み
N, K = map(int, input().split())
P = list(map(int, input().split()))

# 結果を出力
result = solve(N, K, P)
print(" ".join(map(str, result)))
