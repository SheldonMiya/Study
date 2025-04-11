# 正しいカッコ列を再帰的に生成する関数
def generate_parentheses(N, open_count, close_count, current):
    # 基本ケース: 現在のカッコ列が長さ N に達した場合
    if len(current) == N:
        # 現在のカッコ列が有効な正しいカッコ列なので出力
        print(current)
        return
    
    # 開き括弧 '(' を追加できる場合
    if open_count < N // 2:
        # 開き括弧を追加して再帰的に次のカッコ列を生成
        generate_parentheses(N, open_count + 1, close_count, current + '(')
    
    # 閉じ括弧 ')' を追加できる場合
    if close_count < open_count:
        # 閉じ括弧を追加して再帰的に次のカッコ列を生成
        generate_parentheses(N, open_count, close_count + 1, current + ')')

def main():
    N = int(input())  # 標準入力から N を取得
    # N が奇数の場合、正しいカッコ列を作成することはできないので何も出力しない
    if N % 2 != 0:
        return
    # 正しいカッコ列を生成するために再帰関数を呼び出し
    generate_parentheses(N, 0, 0, "")

if __name__ == "__main__":
    main()
