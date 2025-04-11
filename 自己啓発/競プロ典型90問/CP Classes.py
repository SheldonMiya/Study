import bisect

def main():
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [int(input()) for _ in range(Q)]
    
    # クラスレーティング A をソート
    A.sort()
    
    # 各生徒について最小の不満度を計算
    for b in B:
        # bisect_leftで、B[j] よりも大きいまたは等しい最初の位置を見つける
        idx = bisect.bisect_left(A, b)
        
        # 近いレーティングの候補を2つ探す
        best_diff = float('inf')
        
        # 1つ目の候補: A[idx] (idxがAの範囲内であれば)
        if idx < N:
            best_diff = min(best_diff, abs(A[idx] - b))
        
        # 2つ目の候補: A[idx-1] (idx-1が0以上なら)
        if idx > 0:
            best_diff = min(best_diff, abs(A[idx - 1] - b))
        
        # 最小の不満度を出力
        print(best_diff)

if __name__ == "__main__":
    main()
