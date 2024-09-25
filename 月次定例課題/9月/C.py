from itertools import permutations

# エッジセットを構築する関数
def build_edge_set(edges):
    return set((min(u, v), max(u, v)) for u, v in edges)

# グラフのコストを計算する関数
def calculate_cost(h_edges, g_edges, cost_matrix):
    cost = 0
    # 頂点のペアを考慮
    for i in range(N):
        for j in range(i + 1, N):
            # Hにエッジがある場合
            if (i + 1, j + 1) in h_edges:
                # Gにエッジがない場合
                if (i + 1, j + 1) not in g_edges:
                    cost += cost_matrix[i][j]  # コストを追加
            else:  # Hにエッジがない場合
                # Gにエッジがある場合
                if (i + 1, j + 1) in g_edges:
                    cost += cost_matrix[i][j]  # コストを追加
    return cost

# メイン処理
N = int(input())  # 頂点の数
M_G = int(input())  # Gのエッジの数
# Gのエッジをリストに格納
g_edges = [tuple(map(int, input().split())) for _ in range(M_G)]
M_H = int(input())  # Hのエッジの数
# Hのエッジをリストに格納
h_edges = [tuple(map(int, input().split())) for _ in range(M_H)]

# コスト行列の初期化
cost_matrix = [[0] * (N + 1) for _ in range(N + 1)]

# コスト行列の読み込み
for i in range(1, N):
    costs = list(map(int, input().split()))
    for j in range(i + 1, N + 1):
        cost_matrix[i][j] = costs[j - 1 - i]  # コストを設定
        cost_matrix[j][i] = costs[j - 1 - i]  # 無向グラフなので対称に設定

# Gのエッジセットを作成
g_edge_set = build_edge_set(g_edges)

# 最小コストを初期化
min_cost = float('inf')

# Hの頂点の全順列を考慮
for perm in permutations(range(1, N + 1)):
    new_h_edges = set()
    for a, b in h_edges:
        new_a = perm[a - 1]  # 頂点の置き換え
        new_b = perm[b - 1]  # 頂点の置き換え
        new_h_edges.add((min(new_a, new_b), max(new_a, new_b)))  # 順序を保って追加

    # コストを計算
    cost = calculate_cost(new_h_edges, g_edge_set, cost_matrix)
    min_cost = min(min_cost, cost)  # 最小コストを更新
    
# 結果を出力
print(min_cost)
