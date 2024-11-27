def find_bill_combination(N, Y):
    # 10000円札、5000円札、1000円札の最大枚数
    max_10000 = min(N, Y // 10000)
    
    for x in range(max_10000 + 1):
        remaining_y = Y - (x * 10000)
        remaining_n = N - x
        
        # 5000円札の最大枚数を計算
        max_5000 = min(remaining_n, remaining_y // 5000)
        
        for y in range(max_5000 + 1):
            z = remaining_n - y  # 1000円札の枚数
            total_y = x * 10000 + y * 5000 + z * 1000
            
            if z >= 0 and total_y == Y:
                return x, y, z
    
    return -1, -1, -1

# 入力の読み込み
N = int(input())
Y = int(input())

# 組み合わせを探して出力
result = find_bill_combination(N, Y)
print(*result)
