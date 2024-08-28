def is_right_triangle(ax, ay, bx, by, cx, cy):
    # 各辺の長さの二乗を計算
    ab2 = (ax - bx) ** 2 + (ay - by) ** 2
    bc2 = (bx - cx) ** 2 + (by - cy) ** 2
    ca2 = (cx - ax) ** 2 + (cy - ay) ** 2

    # 直角三角形の条件をチェック
    if ab2 + bc2 == ca2 or ab2 + ca2 == bc2 or bc2 + ca2 == ab2:
        return "Yes"
    else:
        return "No"

# 標準入力からデータを受け取る
ax, ay = map(int, input("点Aの座標を入力してください (xA yA): ").split())
bx, by = map(int, input("点Bの座標を入力してください (xB yB): ").split())
cx, cy = map(int, input("点Cの座標を入力してください (xC yC): ").split())

# 直角三角形かどうかを判定して出力
print(is_right_triangle(ax, ay, bx, by, cx, cy))
