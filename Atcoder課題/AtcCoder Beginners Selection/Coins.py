A = int(input())
B = int(input())
C = int(input())
X = int(input())

def count_ways(A, B, C, X):
    ways = 0

    for a in range(A + 1):
        for b in range(B + 1):
            for c in range(C + 1):
                total = a * 500 + b * 100 + c * 50
                if total == X:
                    ways += 1

    return ways

print(count_ways(A, B, C, X))