import sys


def main():
	data = sys.stdin.read().split()
	if not data:
		return

	n = int(data[0])
	records = set()
	for i in range(n):
		student = data[1 + 2 * i]
		booth = data[2 + 2 * i]
		records.add((student, booth))

	stamp_counts = {}
	for student, booth in records:
		stamp_counts[student] = stamp_counts.get(student, 0) + 1

	leaderboard = list(stamp_counts.items())
	leaderboard.sort(key=lambda entry: (-entry[1], entry[0]))

	output = [str(len(records))]
	output.extend(f"{student} {count}" for student, count in leaderboard)
	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
