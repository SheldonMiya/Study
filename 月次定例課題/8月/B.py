def format_number(X):
    # 入力を文字列に変換してから不要な末尾の '0' と '.' を削除
    formatted_X = '{:.3f}'.format(X).rstrip('0').rstrip('.')
    return formatted_X

# 入力
X = float(input("実数 X: "))

print(format_number(X))


# 参考先
## formatメソッドの使い方 → https://gammasoft.jp/blog/python-string-format/#float-point　
## stripメソッドの使い方 → https://inouelog.com/python-strip/
