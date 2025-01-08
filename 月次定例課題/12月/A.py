# 入力の読み込み
N = int(input())  # 水を追加する回数
water = 0  # 加湿器に入っている水の量（初期状態は0リットル）

# 最後の時刻の情報
last_time = 0

for _ in range(N):
    T, V = map(int, input().split())  # 時刻T、追加される水V

    # 水が減る時間の計算
    water -= (T - last_time)  # 前の水追加から現在までの時間差だけ水が減る

    # 水が減った分が0未満にならないように調整
    if water < 0:
        water = 0
    
    # 現在の水量に新たにVリットルを追加
    water += V
    
    # 次の追加時刻を記録
    last_time = T

# 最終的な水の量を出力
print(water)

