# おもちゃの数を入力
N = int(input())

toy_size = sorted(map(int, input().split()), reverse=True)

box_size = sorted(map(int, input().split()), reverse=True)

# 新しい箱のサイズの候補を初期化
ans = 0
# 既存の箱のインデックスを初期化
j = 0

# おもちゃのサイズリストを確認する
for i, toy_size_i in enumerate(toy_size):
    if j >= len(box_size):
        ans = toy_size_i if i == j else -1
    elif toy_size_i <= box_size[j]:
        j += 1
    elif i == j:
        ans = toy_size_i
    else:
        exit(print(-1))

print(ans)
