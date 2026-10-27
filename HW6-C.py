goal = int(input())
steps = list(map(int, input().split()))

print(sum(steps))

qualified_days = 0
longest_streak = 0
current_streak = 0
for step in steps:
	if step >= goal:
		qualified_days += 1
		current_streak += 1
		longest_streak = max(longest_streak, current_streak)
	else:
		current_streak = 0

print(qualified_days)

highest = max(steps)
highest_days = []
for day in range(7):
	if steps[day] == highest:
		highest_days.append(str(day + 1))
print(" ".join(highest_days))

print(longest_streak)
