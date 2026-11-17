import sys


def main():
	data = sys.stdin.read().split()
	n, m = map(int, data[:2])
	club_a = set(data[2:2 + n])
	club_b = set(data[2 + n:2 + n + m])

	results = [
		club_a & club_b,
		club_a | club_b,
		club_a - club_b,
		club_b - club_a,
	]

	for result in results:
		names = sorted(result)
		print(" ".join(names) if names else "NONE")


if __name__ == "__main__":
	main()
