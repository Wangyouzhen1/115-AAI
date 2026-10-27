import sys

B, N, R, C = map(int, sys.stdin.readline().split())
total = max(0, B + B * R // 100 - C)
q, b = divmod(total, N)
a = N - b

print(total)
print(q, a)
print(q + 1, b)
