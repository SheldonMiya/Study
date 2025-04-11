X = int(input())

# 九九の表に書かれる81個の整数の総和を計算
total_sum = sum(i * j for i in range(1, 10) for j in range(1, 10))

# Xを除いた整数の総和を計算
X_count = sum(1 for i in range(1, 10) for j in range(1, 10) if i * j == X)

# もしXが含まれていればその部分を引く
result = total_sum - X * X_count

# 結果を出力
print(result)
