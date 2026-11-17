import sys


def main():
	read = sys.stdin.readline
	n = int(read().strip())
	playlist = read().split() if n > 0 else []

	q = int(read().strip())
	for _ in range(q):
		command = read().strip().split(maxsplit=1)
		if command[0] == "ADD":
			playlist.append(command[1])
		elif command[0] == "REMOVE":
			if command[1] in playlist:
				playlist.remove(command[1])
		else:  # REVERSE
			playlist.reverse()

	print(len(playlist))
	print(" ".join(playlist) if playlist else "EMPTY")


if __name__ == "__main__":
	main()
