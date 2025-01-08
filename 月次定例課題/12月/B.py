from itertools import combinations

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve():
    # 入力の読み込み
    H, W, D = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    
    # 床のマスをリストアップ
    floor_positions = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                floor_positions.append((i, j))
    
    # 加湿器を置く2つの床のマスの組み合わせ
    max_humidified = 0
    
    # 全ての床のマスの組み合わせを考える
    for (x1, y1), (x2, y2) in combinations(floor_positions, 2):
        humidified = set()  # 加湿されるマスの集合
        
        # 1つ目の加湿器による加湿範囲
        for i in range(H):
            for j in range(W):
                if manhattan_distance(x1, y1, i, j) <= D:
                    if grid[i][j] == '.':
                        humidified.add((i, j))
        
        # 2つ目の加湿器による加湿範囲
        for i in range(H):
            for j in range(W):
                if manhattan_distance(x2, y2, i, j) <= D:
                    if grid[i][j] == '.':
                        humidified.add((i, j))
        
        # 現在の組み合わせで加湿される最大のマス数
        max_humidified = max(max_humidified, len(humidified))
    
    print(max_humidified)

# 実行
solve()
