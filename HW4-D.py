hours = int(input())

fee = min(hours, 2) * 30
fee += max(0, min(hours - 2, 3)) * 20
fee += max(0, hours - 5) * 10

print(fee)
