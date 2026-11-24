N = int(input())
value = N
pass_number = 1

while value > 9:
	value = sum(int(digit) for digit in str(value))
	print(f"Pass {pass_number} : {value}")
	pass_number += 1

print(f"Digital Root of {N} : {value}")
