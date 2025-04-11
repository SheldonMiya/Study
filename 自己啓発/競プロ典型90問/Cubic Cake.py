import math

def main():
    # 入力の読み込み
    A, B, C = map(int, input().split())
    
    # 直方体の辺の最大公約数 (GCD) を求める
    gcd = math.gcd(math.gcd(A, B), C)
    
    # 各辺をGCDの長さに分割するための切断回数を計算
    cuts_A = (A // gcd) - 1
    cuts_B = (B // gcd) - 1
    cuts_C = (C // gcd) - 1
    
    # 必要な切断回数の合計
    total_cuts = cuts_A + cuts_B + cuts_C
    
    # 出力
    print(total_cuts)

if __name__ == "__main__":
    main()
