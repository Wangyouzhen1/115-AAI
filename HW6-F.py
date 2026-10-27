import sys

k = int(sys.stdin.readline())
message = sys.stdin.readline().rstrip("\n")

encrypted = []
for char in message:
	code = ord(char)
	if ord("A") <= code <= ord("Z"):
		encrypted.append(chr((code - ord("A") + k) % 26 + ord("A")))
	elif ord("a") <= code <= ord("z"):
		encrypted.append(chr((code - ord("a") + k) % 26 + ord("a")))
	else:
		encrypted.append(char)

print("".join(encrypted))
