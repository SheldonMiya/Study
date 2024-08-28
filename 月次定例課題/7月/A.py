def find_min_pen_price(R, G, B, C):
    # 色に対応するペンの価格を辞書に格納
    pen_prices = {
        "Red": R,
        "Green": G,
        "Blue": B
    }

    # 高橋君が嫌いな色を辞書から削除
    del pen_prices[C]

    # 残ったペンの価格の最小値を返す
    return min(pen_prices.values())

# 入力を受け取る
R = int(input("赤色のペンの価格を入力してください: "))
G = int(input("緑色のペンの価格を入力してください: "))
B = int(input("青色のペンの価格を入力してください: "))
C = input("高橋君が嫌いな色を入力してください (Red, Green, Blue): ").strip()

# 最小価格を計算して出力
print(find_min_pen_price(R, G, B, C))
