n = int(input())

previous_value = 0
current_value = 1

for step in range(n):
	previous_value, current_value = current_value, previous_value + current_value

print(previous_value)
