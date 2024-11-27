def solve(N, S):
    # コストを格納するリスト
    result = []
    
    # 最初の文字列については、自分を空文字列にするコストが必要
    result.append(len(S[0]))  # 最初の文字列はその長さだけ削除すれば空文字列
    
    # 2番目以降の文字列について
    for k in range(1, N):
        min_cost = float('inf')
        
        # 現在の文字列 S[k] をそれ以前の文字列 S[1], S[2], ..., S[k-1] に一致させるコストを計算
        for i in range(k):
            # 2つの文字列 S[i] と S[k] の最長共通接頭辞を求める
            common_len = 0
            while common_len < len(S[i]) and common_len < len(S[k]) and S[i][common_len] == S[k][common_len]:
                common_len += 1
            
            # S[k] を S[i] に合わせるためのコストは、削除した後、追加するコスト
            cost = len(S[i]) - common_len + len(S[k]) - common_len  # 削除と追加
            min_cost = min(min_cost, cost)
        
        # k 番目の結果を保存
        result.append(min_cost)
    
    return result

# 入力の読み込み
N = int(input())
S = [input().strip() for _ in range(N)]

# 結果の計算
result = solve(N, S)

# 結果を出力
for cost in result:
    print(cost)