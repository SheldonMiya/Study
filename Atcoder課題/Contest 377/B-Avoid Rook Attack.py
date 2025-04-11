# 入力の読み込み
board = [input().strip() for _ in range(8)]

# コマが置かれている行・列を記録するためのリスト
blocked_rows = set()  # コマが置かれている行
blocked_cols = set()  # コマが置かれている列

# 盤面を確認して、コマが置かれている行・列を記録
for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            blocked_rows.add(i)  # コマが置かれている行
            blocked_cols.add(j)  # コマが置かれている列

# 空いている場所にコマを置けるかどうかを確認
count = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == '.' and i not in blocked_rows and j not in blocked_cols:
            count += 1

# 結果を出力
print(count)
