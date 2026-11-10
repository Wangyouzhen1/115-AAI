def is_prime(n):
	if n < 2:
		return False

	divisor = 2
	while divisor * divisor <= n:
		if n % divisor == 0:
			return False
		divisor += 1
	return True


def main():
	L, R = map(int, input().split())
	primes = []
	for number in range(L, R + 1):
		if is_prime(number):
			primes.append(number)

	print(*primes) if primes else print("NONE")
	print(len(primes), sum(primes))


if __name__ == "__main__":
	main()
