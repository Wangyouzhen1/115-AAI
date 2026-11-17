import sys


def main():
	data = sys.stdin.read().split()
	if not data:
		return

	n = int(data[0])
	records = []
	user_items = {}

	pos = 1
	for _ in range(n):
		user = data[pos]
		item = data[pos + 1]
		pos += 2
		records.append((user, item))
		user_items.setdefault(user, set()).add(item)

	target = data[pos]
	k = int(data[pos + 1])
	target_items = user_items[target]

	scores = {}
	for user, items in user_items.items():
		if user != target and target_items.intersection(items):
			for item in items.difference(target_items):
				scores[item] = scores.get(item, 0) + 1

	ranked = sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))
	recommendations = ranked[:k]
	if not recommendations:
		print(0)
		return

	print(len(recommendations))
	for item, score in recommendations:
		print(item, score)


if __name__ == "__main__":
	main()
