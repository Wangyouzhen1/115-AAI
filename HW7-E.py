import sys


def count_ways(step, n, blocked, memo):
	if step > n or blocked[step]:
		return 0
	if step == n:
		return 1
	if memo[step] != -1:
		return memo[step]

	memo[step] = count_ways(step + 1, n, blocked, memo) + count_ways(
		step + 2, n, blocked, memo
	)
	return memo[step]


def main():
	values = list(map(int, sys.stdin.buffer.read().split()))
	if not values:
		return

	n, k = values[0], values[1]
	blocked = [False] * (n + 1)
	for stair in values[2:2 + k]:
		blocked[stair] = True

	memo = [-1] * (n + 1)
	print(count_ways(0, n, blocked, memo))


if __name__ == "__main__":
	main()
