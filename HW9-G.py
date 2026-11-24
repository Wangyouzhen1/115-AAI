import sys


lines = sys.stdin.read().splitlines()
if len(lines) >= 2:
	keys = [int(value) for value in lines[0].split()]
	ciphertext = lines[1]

	if keys:
		result = []
		letter_index = 0
		for char in ciphertext:
			if "A" <= char <= "Z":
				shift = keys[letter_index % len(keys)]
				result.append(chr((ord(char) - ord("A") - shift) % 26 + ord("A")))
				letter_index += 1
			elif "a" <= char <= "z":
				shift = keys[letter_index % len(keys)]
				result.append(chr((ord(char) - ord("a") - shift) % 26 + ord("a")))
				letter_index += 1
			else:
				result.append(char)

		print("".join(result))
