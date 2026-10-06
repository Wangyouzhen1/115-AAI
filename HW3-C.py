# 讀取三個整數
x1, x2, x3 = map(int, input().split())

# 平均數與母體變異數
mean = (x1 + x2 + x3) / 3
variance = ((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2) / 3

# 輸出，保留兩位小數
print(f"{mean:.2f}")
print(f"{variance:.2f}")
