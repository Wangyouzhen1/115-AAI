import sys


def normalize(text):
	result = []
	for char in text:
		if "A" <= char <= "Z":
			result.append(char.lower())
		elif "a" <= char <= "z" or "0" <= char <= "9":
			result.append(char)
	return "".join(result)


def is_palindrome(text, left, right):
	if left >= right:
		return True
	if text[left] != text[right]:
		return False
	return is_palindrome(text, left + 1, right - 1)


line = sys.stdin.readline()
if line.endswith("\n"):
	line = line[:-1]

cleaned = normalize(line)
print("YES" if is_palindrome(cleaned, 0, len(cleaned) - 1) else "NO")
