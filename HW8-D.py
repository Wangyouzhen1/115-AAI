import sys


def main():
	data = sys.stdin.read().split()
	if not data:
		return

	index = 0
	n = int(data[index])
	index += 1

	inventory = {}
	for _ in range(n):
		item = data[index]
		stock = int(data[index + 1])
		index += 2
		inventory[item] = stock

	q = int(data[index])
	index += 1

	sold = 0
	rejected = 0
	for _ in range(q):
		operation = data[index]
		item = data[index + 1]
		qty = int(data[index + 2])
		index += 3

		if operation == "ADD":
			inventory[item] = inventory.get(item, 0) + qty
		elif item in inventory and inventory[item] >= qty:
			inventory[item] -= qty
			sold += qty
		else:
			rejected += 1

	output = [f"{sold} {rejected}"]
	for item in sorted(inventory):
		output.append(f"{item} {inventory[item]}")
	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
