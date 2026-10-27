menu_count = int(input())
drink_names = []
prices = []
drink_totals = []

for _ in range(menu_count):
	drink, price = input().split()
	drink_names.append(drink)
	prices.append(int(price))
	drink_totals.append(0)

order_count = int(input())
order_students = []
order_drinks = []
order_quantities = []
student_names = []
student_totals = []

for _ in range(order_count):
	student, drink, quantity = input().split()
	quantity = int(quantity)
	order_students.append(student)
	order_drinks.append(drink)
	order_quantities.append(quantity)

	drink_index = drink_names.index(drink)
	drink_totals[drink_index] += quantity

	if student not in student_names:
		student_names.append(student)
		student_totals.append(0)

for i in range(order_count):
	student_index = student_names.index(order_students[i])
	drink_index = drink_names.index(order_drinks[i])
	unit_price = prices[drink_index]
	if drink_totals[drink_index] >= 10:
		unit_price -= 5
	student_totals[student_index] += unit_price * order_quantities[i]

for i in range(menu_count):
	print("DRINK", drink_names[i], drink_totals[i])

for i in range(len(student_names)):
	print("STUDENT", student_names[i], student_totals[i])

print("TOTAL", sum(student_totals))
