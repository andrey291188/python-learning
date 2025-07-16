import math

# Для чисел з точкою
bet = int(input("Скільки грошей ставимо? "))
coefficient = float(input("Який коефіцієнт? "))

win = bet * coefficient 

print("Потенційний виграш:", win)

# round окруклюємо до двох знаків після точки
bet = int(input("Скільки грошей ставимо? "))
coefficient = float(input("Який коефіцієнт? "))

win = bet * coefficient 

print("Потенційний виграш:", round(win, 2))

# Індекс маси тіла, практика з точкою в числі
height = float(input("Ваш зріст: "))
weight = float(input("Ваша вага: "))

bmi = round(weight / height ** 2, 2)

print("Ідекс маси вашого тіла:", bmi)

if bmi < 18.5:
    print("У вас недостатня маса тіла")
elif bmi < 25:
    print("У вас нормальна маса тіла")
elif bmi < 30:
    print("У вас надлишкова вага")
else:
    print("У вас надто надлишкова")

# Щоб з дробного числа отримати ціле
number = 256.12314

print("Ціле число", int(number))

# Робота з модулем math
x = int(input("Введіть координату х: "))
y = int(input("Введіть координату y: "))

distance = math.sqrt(x ** 2 + y ** 2)

print("Дистанція: ", distance)