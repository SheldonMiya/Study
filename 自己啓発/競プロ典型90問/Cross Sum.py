def main():
    # 入力を受け取る
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    
    # 行ごとの合計を計算
    row_sum = [sum(A[i]) for i in range(H)]
    
    # 列ごとの合計を計算
    col_sum = [sum(A[i][j] for i in range(H)) for j in range(W)]
    
    # 各マスに対する結果を計算して出力
    for i in range(H):
        for j in range(W):
            # 各マス (i, j) に対する B[i][j] の計算
            result = row_sum[i] + col_sum[j] - A[i][j]
            print(result, end=" ")
        print()

if __name__ == "__main__":
    main()
