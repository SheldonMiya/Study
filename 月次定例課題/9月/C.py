# 公式解説 
## https://www.youtube.com/watch?v=-vsRrFtN8eo&t=2077s

# ノードの数
N = int(input())

# グラフを受け取る関数
def getEdges():
  M = int(input())
  Edges = [[False]*N for _ in range(N)]
  
  for _ in range(M):
    u, v = map(int, input().split())
    # 0-indexed
    u -= 1
    v -= 1
    
    Edges[u][v] = True
  
  return Edges

# Gを構築
G = getEdges()

# Hを構築
H = getEdges()

# Aを構築
A = [list(map(int, input().split())) for _ in range(N-1)]

import itertools


ans = float("inf")
# 頂点を入れ替える
for table in itertools.permutations(range(N)):
  # コストの計算
  tmp = 0
  # 辺の有無を全て確認する．
  for i in range(N):
    for j in range(N):
      # 重複を防ぐ
      if(i>=j):continue
      # 並び替えを考慮する(I<Jとする)
      I = min(table[i], table[j])
      J = max(table[i], table[j])
      
      # 辺の有無が一致しない時
      if(G[I][J] != H[i][j]):
        tmp += A[i][j-i-1]
        
  # 最小コストの更新
  ans = min(ans, tmp)
  
print(ans)
