def main():
    # 家の数と赤子の数を取得
    N, M = map(int, input().split())
    
    # 各家の男の子が生まれたかどうかを記録
    first_born = [None] * (N + 1)  # 家番号は1から
    
    # 判定結果を格納リスト
    results = []
    
    for i in range(1, M + 1):
        A_i, B_i = input().split()
        A_i = int(A_i)
        
        if B_i == 'M':  # 男の子の場合
            if first_born[A_i] is None:  # まだ生まれていない場合
                first_born[A_i] = i  # 現在の赤子のインデックスを記録
                results.append("Yes")
            else:
                results.append("No")  # 既に生まれた男の子がいるので「太郎」ではない
        else:  # 女の子の場合
            results.append("No")  # 女の子は「太郎」ではない

    # 結果を出力
    print("\n".join(results))

# 実行部分
if __name__ == "__main__":
    main()