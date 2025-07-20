count = int(input("Скільки грошей на рахунку? "))

# Умовний оператор if
# Порівняння більше
if count > 100:
    print('Порівняння більше!')

# Порівняння менше
if count < 100:
    print('Порівняння менше!')

# Порівняння дорівнює 
if count == 100:
    print('Порівняння дорівнює!')

# Порівняння не дорівнює 
if count != 100:
    print('Порівняння не дорівнює!')

# Порівняння менше або дорівнює 
if count <= 100:
    print('Порівняння менше або дорівнює!')

# Порівняння більше або дорівнює 
if count >= 100:
    print('Порівняння більше або дорівнює!')

# Форма if та else 
if count > 100:
    print('Порівняння більше!')
else:
    print('Порівняння менше!')

# Вкладений if у if
if count > 100:

    count -= 80
    print('Порівняння більше!')

    if count < 50:
        count += 50
        print('Зроблена знижка, ваш рахунок', count)

else:
    print('Порівняння менше!')

# Форма if,elif та else
x = int(input("Введіть число х: "))
y = int(input("Введіть число y: "))

if x > y:
    print("x більше y")
elif x < y:
    print("x менше y")
else:
    print("x дорівнює y")

# Оператор and в умові if
year = int(input("Введіть рік: "))
speed_count = int(input("Введіть швидкість: "))

if year >= 2018 and speed_count >= 24:
    print("Підходить")
else: 
    print("Не підходить")

# Оператор or в умові if
if year < 2018 or speed_count < 24:
    print("Не підходить")
else: 
    print("Підходить")
 

# Декілька логічних операторів в умові
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Рік високосний")
else: 
    print("Рік не високосний")