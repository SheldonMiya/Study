import itertools

def main():
    # 入力の読み込み
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 5個を選ぶ組み合わせを列挙
    count = 0
    for comb in itertools.combinations(A, 5):
        # 5個の積を計算し、その積をPで割った余りがQであるかチェック
        product = 1
        for num in comb:
            product = (product * num) % P  # 積をPで割った余りを計算
        
        if product == Q:
            count += 1
    
    # 結果の出力
    print(count)

if __name__ == "__main__":
    main()