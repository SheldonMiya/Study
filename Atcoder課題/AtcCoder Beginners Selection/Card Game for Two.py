def calculate_score_difference(N, cards):
    # カードを得点の高い順にソート
    cards.sort(reverse=True)
    
    alice_score = 0
    bob_score = 0
    
    # Alice と Bob が交互にカードを取る
    for i in range(N):
        if i % 2 == 0:  # Alice のターン
            alice_score += cards[i]
        else:           # Bob のターン
            bob_score += cards[i]
    
    # 得点差を計算
    score_difference = alice_score - bob_score
    return score_difference

# 入力の読み込み
N = int(input())
cards = list(map(int, input().split()))

# スコア差を計算して出力
result = calculate_score_difference(N, cards)
print(result)
