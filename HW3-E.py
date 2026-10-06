import sys

values = list(map(int, sys.stdin.read().split()))
a, b, c, d, e, f, g, h = values

print(a * e + b * g, a * f + b * h)
print(c * e + d * g, c * f + d * h)
