import sys


values = sys.stdin.read().split()
if len(values) >= 2:
	a, b = map(int, values[:2])
	total = a + b
	print(f"{a}+{b}={total}")
