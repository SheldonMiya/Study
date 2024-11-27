N, K = map(int, input().split())
S = input()

def solve(N, K, S):
    # 1の塊を特定する
    ones_blocks = []
    i = 0
    while i < N:
        if S[i] == '1':
            start = i
            while i < N and S[i] == '1':
                i += 1
            end = i - 1
            ones_blocks.append((start, end))
        else:
            i += 1

    # K 番目の 1 の塊を移動
    # K 番目の塊を K-1 番目の塊の直後に移動
    start_k, end_k = ones_blocks[K-1]
    start_k_1, end_k_1 = ones_blocks[K-2]

    # 新しい位置の決定
    new_start = end_k_1 + 1
    new_end = new_start + (end_k - start_k)

    # 新しい文字列を作成する
    result = list(S)

    # K 番目の 1 の塊を K-1 番目の直後に移動
    # 最初に、K 番目の 1 の塊を消去
    for i in range(start_k, end_k + 1):
        result[i] = '0'
    
    # 新しい位置に 1 をセット
    for i in range(new_start, new_end + 1):
        result[i] = '1'

    return ''.join(result)

print(solve(N, K, S))
