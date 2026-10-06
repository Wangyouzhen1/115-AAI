n = int(input())

hundreds = n // 100
remainder = n % 100
tens = remainder // 10
units = remainder % 10

print(hundreds, tens, units)
print(hundreds + tens + units)
print(hundreds * tens * units)
print(int(str(units) + str(tens) + str(hundreds)))
