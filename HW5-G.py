import sys

total = 0
line = sys.stdin.readline()
while line:
	value = int(line)
	if value == 0:
		break
	total += value
	line = sys.stdin.readline()

print(total)
