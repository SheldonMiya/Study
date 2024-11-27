N, A, B = map(int, input().split())

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def calculate_sum(N, A, B):
    total_sum = 0
    for i in range(1, N + 1):
        d_sum = digit_sum(i)
        if A <= d_sum <= B:
            total_sum += i
    return total_sum

print(calculate_sum(N, A, B))
