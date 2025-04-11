def main():
    # 入力の読み込み
    N = int(input())  # 生徒の数
    C = []  # クラス
    P = []  # 点数
    
    for _ in range(N):
        c, p = map(int, input().split())
        C.append(c)
        P.append(p)
    
    Q = int(input())  # クエリの数
    queries = []
    for _ in range(Q):
        L, R = map(int, input().split())
        queries.append((L - 1, R - 1))  # 0-based indexに変換
    
    # クラスごとの累積和を計算
    sum1 = [0] * (N + 1)  # 1組の累積和
    sum2 = [0] * (N + 1)  # 2組の累積和
    
    for i in range(N):
        if C[i] == 1:
            sum1[i + 1] = sum1[i] + P[i]
            sum2[i + 1] = sum2[i]
        else:
            sum2[i + 1] = sum2[i] + P[i]
            sum1[i + 1] = sum1[i]
    
    # クエリに答える
    for L, R in queries:
        A = sum1[R + 1] - sum1[L]  # 1組の合計
        B = sum2[R + 1] - sum2[L]  # 2組の合計
        print(A, B)

if __name__ == "__main__":
    main()
