# 1. 讀取輸入的正整數 n
n = int(input())

# 2. 建立累加總和的變數，初始值設為 0
total = 0

# 3. 使用 for 迴圈從 1 累加到 n
# 注意：range(1, n + 1) 會包含 1 到 n
for i in range(1, n + 1):
    total += i  # 等同於 total = total + i

# 4. 輸出最終結果
print(total)