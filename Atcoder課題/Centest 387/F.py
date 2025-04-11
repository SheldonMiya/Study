N, M = map(int, input().split())
A = list(map(int, input().split()))

# dp[i] は x_i が i の場合の組み合わせの数を保持
dp = [1] * (M + 1)

# 通り数を計算
for i in range(N):
    # 現在の状態を保存
    new_dp = [0] * (M + 1)
    for x in range(1, M + 1):
        if x <= x[A[i] - 1]:
            new_dp[x] = sum(dp[:x]) % 998244353

    dp = new_dp

# 結果を出力
print(dp[0])
