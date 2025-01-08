# ヘビ数の判定関数
def is_heavy_number(n):
    digits = list(map(int, str(n)))  # 数字をリストに変換
    first_digit = digits[0]  # 最初の桁を取り出す
    return all(first_digit > digit for digit in digits[1:])  # 最初の桁より大きい桁がないかチェック

# 入力を受け取る
L, R = map(int, input().split())

# ヘビ数の個数を数える
count = 0
for num in range(L, R + 1):
    if is_heavy_number(num):
        count += 1

# 結果を出力
print(count)
