# 基本輸出
print('Hello, World!')
print('Python', '程式設計')

# 自訂分隔符號
print(10, 20, 30, sep='+')

# 不換行輸出
print('Hello', end=' ')
print('Python')

print('第一行\n第二行')
print('姓名\t年齡\t身高')
print('It\'s a sunny day')
print("他說：\"你好\"")


# 學生成績格式化輸出範例
a, b, c = map(int, input('請輸入三個數字(用空格分隔)：').split())

name = input('請輸入學生姓名：')
chinese = float(input('請輸入國文成績：'))
english = float(input('請輸入英文成績：'))
math = float(input('請輸入數學成績：'))

print(f'學生姓名：{name}')
print(f'國文成績：{chinese:6.1f}分')
print(f'英文成績：{english:6.1f}分')
print(f'數學成績：{math:6.1f}分')
print(f'平均成績：{(chinese+english+math)/3:6.2f}分')
