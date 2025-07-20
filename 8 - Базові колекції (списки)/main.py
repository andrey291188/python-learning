# Список та додавання чисел в список
numbers = [] # Список

for number in range(100):
    numbers.append(number) # Додавання числа в список

print(numbers)

# Звертання до змінной в списку
numbers = [1, 2, 3, 4, 5]

number = numbers[2] 

print(number) # Виведе 3

# Переприсвоення значення в списку
numbers = [1, 2, 3, 4, 5]

numbers[2] *= 2

print(numbers[2]) # Виведе 6

# Перетворюємо в список строку
word = "Hello world"

sym_list = list(word)

print(sym_list)

# Отримати довжину списку
new_list = [1, 2, 3, 4, 5, 6, 7]

length_list = len(new_list)

print(length_list)

# Вивести останній елемент списку
new_list = [1, 2, 3, 4, 5, 6, 7]

last_element = len(new_list) - 1

print(new_list[last_element]) # new_list[-1] альтернатива
