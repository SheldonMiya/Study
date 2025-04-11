def can_divide_with_score(segments, N, K, score):
    # 現在のスコアで分けられるかを判定する関数
    count = 0
    last_cut = 0  # 最後の切れ目位置
    for i in range(N):
        if segments[i] - last_cut >= score:
            count += 1
            last_cut = segments[i]
        if count >= K:
            return True
    return False

def main():
    N, L = map(int, input().split())
    K = int(input())
    cuts = list(map(int, input().split()))
    
    # 切れ目位置をリストに入れます
    cuts = [0] + cuts + [L]
    
    # 各区間の長さを計算します
    segments = []
    for i in range(1, len(cuts)):
        segments.append(cuts[i] - cuts[i-1])
    
    # 二分探索でスコアを最大化する
    low, high = 1, L
    best_score = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_divide_with_score(segments, N, K, mid):
            best_score = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(best_score)

if __name__ == "__main__":
    main()
