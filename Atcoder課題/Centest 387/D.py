# n の桁和を計算する関数
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

# n が良い整数かどうかを判定する関数
def is_good_integer(n):
    return n % digit_sum(n) == 0

N = int(input())

# 双子の良い整数 (a, a+1) を探す
for a in range(N, 2 * N):
    if is_good_integer(a) and is_good_integer(a + 1):
        print(a)
        break
else:
    print(-1)
