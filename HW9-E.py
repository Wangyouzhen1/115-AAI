N = int(input())
current = N
pass_number = 1

while True:
	current = sum(int(digit) for digit in str(current))
	print(f"Pass {pass_number} : {current}")
	if current < 10:
		break
	pass_number += 1

print(f"Digital Root of {N} : {current}")
