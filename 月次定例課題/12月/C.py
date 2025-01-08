from collections import deque

# 幅優先探索 (BFS)
def bfs(H, W, D, grid, start_points):
    # 4方向 (上下左右)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 加湿されたマスを管理する集合
    humidified = set()
    
    # キューに加湿器の位置を追加
    queue = deque()
    for start in start_points:
        queue.append((start[0], start[1], 0))  # (x, y, 距離)
        humidified.add((start[0], start[1]))  # 加湿器の場所は必ず加湿される

    # BFS探索
    while queue:
        x, y, dist = queue.popleft()
        
        # 現在の距離がDを超えたらそれ以上探索しない
        if dist >= D:
            continue
        
        # 4方向に移動して探索
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 範囲外チェック
            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] == '.' and (nx, ny) not in humidified:
                    humidified.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
    
    return len(humidified)

def solve():
    # 入力を読み込む
    H, W, D = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    
    # 加湿器の場所を探す
    start_points = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'H':
                start_points.append((i, j))
    
    # BFSで加湿されたマスの数を求める
    result = bfs(H, W, D, grid, start_points)
    
    # 結果を出力
    print(result)

# 実行
solve()
