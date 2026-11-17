import sys


def main():
	data = sys.stdin.read().split()
	if not data:
		return

	n = int(data[0])
	runners = []
	index = 1
	for _ in range(n):
		name = data[index]
		time = int(data[index + 1])
		penalty = int(data[index + 2])
		runners.append((name, time, penalty))
		index += 3

	runners.sort(key=lambda runner: (runner[1] + runner[2], runner[1], runner[0]))
	output = [f"{name} {time + penalty}" for name, time, penalty in runners]
	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
