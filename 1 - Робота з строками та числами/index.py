# Вивід в консоль даних 
print('Hello world') 

# Для вводу та відображення даних зі зімінної
name = input("Введіть ім'я")
print("Привіт", name)

# Множинне присваювання змінних
first_name, last_name, age = "Andrii", "Zaiac", 37

# Конкатинація 
print(first_name + " " + last_name + " " + "say 'Hello my friend'")


# Заміна місцями значень
a = input("Введіть 1")
b = input("Введіть 2")

print(a,b)

a,b = b,a

print(a,b)

# Математичні дії
print(3 + 4) # Додавання
print(2 - 1) # Вичитання
print(3 / 2) # Ділення
print(3 * 5) # Множення
print(2 ** 3) # Возведення у степінь 

# Приведенення до числа з інпута
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = a + b
print(c)

# Ділення числа на ціле
apples = 41
boxes = 3 
full_boxes = apples // boxes
print(full_boxes)

#Отримати залишок
rest_apples = apples % boxes

# Переприсвоєння змінної
product = 0 
product += 10
product += 100
print(product)
