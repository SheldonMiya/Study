def can_construct(S):
    # 様々な単語のリスト
    words = ["dream", "dreamer", "erase", "eraser"]
    
    # 文字列 S を逆から処理する
    while S:
        found = False
        for word in words:
            if S.endswith(word):
                S = S[:-len(word)]  # word を取り除く
                found = True
                break
        if not found:
            return "NO"  # どの単語も見つからなかった場合
            
    return "YES"  # すべて取り除けた場合

# 入力の読み込み
S = input().strip()

# 判定して出力
result = can_construct(S)
print(result)
