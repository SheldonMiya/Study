from itertools import product

# 入力
N, K = map(int, input().split())
R = list(map(int, input().split()))

# 全ての長さ N の整数列を生成する
results = []
for multiple in product(*[range(1, r + 1) for r in R]):
    if sum(multiple) % K == 0:
        results.append(multiple)

# 辞書順で出力
for result in sorted(results):
    print(*result)


# 参考先
## itertools.product → https://www.math-joy-life.com/python-itertools-product/