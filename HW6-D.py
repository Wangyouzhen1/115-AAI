import sys


data = sys.stdin.read().split()
n = int(data[0])

names = []
subtotals = []
index = 1

for _ in range(n):
	name = data[index]
	price = int(data[index + 1])
	quantity = int(data[index + 2])
	index += 3

	names.append(name)
	subtotals.append((quantity - quantity // 3) * price)

for name, subtotal in zip(names, subtotals):
	print(name, subtotal)

total = sum(subtotals)
if total >= 1000:
	total -= 100
print("TOTAL", total)

top_index = 0
for i in range(1, n):
	if subtotals[i] > subtotals[top_index]:
		top_index = i
print("TOP", names[top_index])
