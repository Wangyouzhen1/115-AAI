usage = int(input())

if usage <= 120:
	bill = usage * 2.10
elif usage <= 500:
	bill = 120 * 2.10 + (usage - 120) * 3.02
else:
	bill = 120 * 2.10 + 380 * 3.02 + (usage - 500) * 4.39

print(f"{bill:.1f}")