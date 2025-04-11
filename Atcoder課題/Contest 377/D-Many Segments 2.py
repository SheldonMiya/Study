def count_valid_pairs(N, M, L, R):
    # 全ての (l, r) のペア数
    total_pairs = M * (M + 1) // 2
    
    # 各区間 [L[i], R[i]] に対して、[l, r] がその区間を完全に含む場合の数を数える
    for i in range(N):
        li = L[i]
        ri = R[i]
        
        # [l, r] が [L[i], R[i]] を完全に含む条件
        # l <= li, r >= ri である必要がある
        # l の範囲は [1, li]
        # r の範囲は [ri, M]
        
        # l が [1, li] の範囲にある
        # r が [ri, M] の範囲にある
        
        valid_l_count = li  # l は 1 から li の範囲
        valid_r_count = M - ri + 1  # r は ri から M の範囲
        
        # この区間に対する含まれる (l, r) のペア数
        contained_pairs = valid_l_count * valid_r_count
        
        # 含まれないペアを引く
        total_pairs -= contained_pairs
    
    return total_pairs

# 入力の読み込み
N, M = map(int, input().split())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# 答えを計算して出力
print(count_valid_pairs(N, M, L, R))
