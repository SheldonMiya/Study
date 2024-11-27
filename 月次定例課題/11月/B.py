S = input()

S = S[1:-1]

A = [len(part) for part in S.split('|')]

print(" ".join(map(str, A)))