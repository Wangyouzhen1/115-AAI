import sys


def parking_fee(minutes):
	if minutes == 0:
		return 0
	return min(((minutes + 29) // 30) * 30, 200)


def main():
	data = list(map(int, sys.stdin.read().split()))
	n = data[0]
	fees = [parking_fee(minutes) for minutes in data[1:1 + n]]
	print(*fees)
	print(sum(fees))


if __name__ == "__main__":
	main()
