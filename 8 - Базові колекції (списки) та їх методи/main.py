# Звертання до змінной в списку
numbers = [1, 2, 3, 4, 5]

number = numbers[2] 

print(number) # Виведе 3

# Переприсвоення значення в списку
numbers = [1, 2, 3, 4, 5]

numbers[2] *= 2

print(numbers[2]) # Виведе 6

# Список та додавання чисел в список
numbers = [] # Список

for number in range(100):
    numbers.append(number) # Додавання числа в список

print(numbers)

# Перетворюємо строку в список
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

# Вставити в середену списка 
langs = ["python", "java", "js", "sql"]

langs.insert(2, "c++")

print(langs)

# Вивести індех елемента в списку
langs = ["python", "java", "js", "sql"]

index_el = langs.index("java")

print(index_el)

# Видалити елемент зі списку
langs = ["python", "java", "js", "sql"]

new_list = langs.remove("java")

print(new_list)

# Об'єднати на списки
first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 0]

first_list.extend(second_list)

print(first_list)

# Заповнити список діапазоном чисел
N = int(input("Кількість людей: "))

members = list(range(1, N + 1))

print(members)
