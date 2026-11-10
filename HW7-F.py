import sys


def best_total(prices, index, remaining):
	if index == len(prices):
		return 0

	best_without = best_total(prices, index + 1, remaining)
	best_with = 0
	if prices[index] <= remaining:
		best_with = prices[index] + best_total(
			prices, index + 1, remaining - prices[index]
		)

	return max(best_without, best_with)


data = list(map(int, sys.stdin.buffer.read().split()))
if data:
	n, budget = data[0], data[1]
	prices = data[2:2 + n]
	print(best_total(prices, 0, budget))
