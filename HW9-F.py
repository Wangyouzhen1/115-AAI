import sys


values = list(map(int, sys.stdin.read().split()))
if len(values) >= 2:
	a, b = sorted(values[:2])
	primes = []
	for number in range(max(2, a), b + 1):
		is_prime = True
		divisor = 2
		while divisor * divisor <= number:
			if number % divisor == 0:
				is_prime = False
				break
			divisor += 1
		if is_prime:
			primes.append(str(number))
	print(" ".join(primes))
