# Кортеж запис
nums = (1, 2, 3, 4, 5) # Зберігає дані в оригінальному вигляді та недає їх змінити
nums_list = list(nums) # Перетворення кортежа в список

# Перетворення списку в кортеж
nums2 = [1, 2, 3, 4, 5]
nums_tuple = tuple(nums2)

print(nums_tuple)

# Запис в кортеж
user = "Volodimir", 'Vasiliev', 25 # Буде кортеж ("Volodimir", 'Vasiliev', 25)
name, surname, age = user # Дістаємо значення з кортежу name = Volodimir",  surname = 'Vasiliev', age = 25

# Функія та кортеж
def get_user():
    name = "Bob"
    surname = "Ivanov"
    age = 30

    return name, surname, age

user = get_user()

print(user) # Виведе кортеж з даними ("Bob", "Ivanov", 30)

# enumerate в циклі
scores = [54, 67, 48, 99, 27]

for i_player in enumerate(scores):
    print(i_player) # Виведе (0, 54) індекс та число згідно списку

for i_player, i_score in enumerate(scores):
    print(i_player, i_score) # Виведе 0, 54 індекс та число згідно списку

# Робота з словарями
score_dict = {
    "Ivan": 33,
    "Petya": 60,
    "Elena": 45
}

for i_name, i_score in score_dict.items():
    print(i_name, i_score)  # Виведе Ivan 33 в кожній ітерації згідно даним

# Кортежи в об'єкті
phonebook_dict = {
    ("Petrov", "Ivan"): 123,
    ("Sidorov", "Petya"): 234,
    ("Egorov", "Ivan"): 345
}

phonebook_dict[("Egorov", "Ivan")] = 567

# zip Функція яка об'єднає два списки
name = ["Tom", "Bob", "Albert"]
ages = [20, 45, 70]

people = dict(zip(name, ages)) # Виведе { "Tom": 20, "Bob": 45, "Albert": 70}