import sys


def main():
	n = int(sys.stdin.readline())
	playlist = sys.stdin.readline().split()
	q = int(sys.stdin.readline())

	for _ in range(q):
		parts = sys.stdin.readline().split()
		if parts[0] == "ADD":
			playlist.append(parts[1])
		elif parts[0] == "REMOVE":
			if parts[1] in playlist:
				playlist.remove(parts[1])
		else:  # REVERSE
			playlist.reverse()

	print(len(playlist))
	print(" ".join(playlist) if playlist else "EMPTY")


if __name__ == "__main__":
	main()
