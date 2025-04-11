# 入力を受け取る
S = input().strip()

# S をソートして、それが 'ABC' と一致するかどうかをチェック
if ''.join(sorted(S)) == 'ABC':
    print('Yes')
else:
    print('No')
