a, b, c = map(int, input().split())
sides = sorted((a, b, c))

if sides[0] + sides[1] <= sides[2]:
	print("Invalid")
elif a == b == c:
	print("Equilateral")
elif a == b or a == c or b == c:
	print("Isosceles")
else:
	print("Scalene")
