def max_mochi_layers(N, diameters):
    # 餅の直径を降順にソート
    diameters.sort(reverse=True)
    
    max_layers = 0
    last_diameter = float('inf')  # 最後に置いた餅の直径を無限大で初期化
    
    for diameter in diameters:
        # 現在の直径が前の直径より小さい場合のみカウント
        if diameter < last_diameter:
            max_layers += 1
            last_diameter = diameter  # 現在の直径を更新
            
    return max_layers

# 入力の読み込み
N = int(input())
diameters = [int(input()) for _ in range(N)]

# 最大段数を計算して出力
result = max_mochi_layers(N, diameters)
print(result)
