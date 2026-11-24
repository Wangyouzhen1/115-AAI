usage = int(input())
if (usage <= 120):
    fee = (usage * 2.10)
elif (usage <= 500):
    fee = (usage * 2.10) + (usage - 120) * 3.02
else:
    (usage >= 500)
    fee = (usage * 2.10) + (usage - 120) * 3.02 + (usage - 500) * 4.39

print (f"{fee:.1f}")