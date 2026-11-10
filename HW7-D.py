def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)


def simplify_recipe(tea, milk, syrup):
	common_divisor = gcd(gcd(tea, milk), syrup)
	return tea // common_divisor, milk // common_divisor, syrup // common_divisor


recipe_count = int(input())
for _ in range(recipe_count):
	tea, milk, syrup = map(int, input().split())
	print(*simplify_recipe(tea, milk, syrup))
