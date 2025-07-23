# Підстановка слов в строку
user_name = input("Введіть ім'я користувача: ")
file_name = input("Введіть назву файла: ")

path = "C:/{user}/docs/folder/{file}.txt".format(user=user_name, file=file_name)

path_index = "C:/{0}/docs/folder/{1}.txt".format(user_name, file_name) # Підстановка по індексам

path_1 = f"C:/{user_name}/docs/folder/{file_name}.txt" # Підстановка по значенням через f-strings

path.endswith(".txt") # Перервірка на що закінчуется шлях
path.startswith("C:/") # Перевірка на що починається строка

print("Шлях до файлу:", path)

# Метод спілт перетворю слова в рядку в масив слів
text = input("Введіть речення: ")

word_list = text.split() # стандартний роздільник це " ", split(",") роздільник кома

print(word_list)

# Метод join збирає масив слів в строку
new_text = "---".join(word_list)

print(new_text)

# Приведення слів до нижнього регістра
name = "ANDRII"
name2 = "andrii2"

new_name = name.lower() # До нижнього регістра
new_name2 = name2.upper() # До верхнього регістра

print(name)
print(name2) 

# Детальний розбір роботи з методом format
details_sum = 5000000
price = 23.8589578
increase = 0.045678

print("На складі {:,d} деталей".format(details_sum)) # Вивод суми 5,000,000
print("Кожна деталь коштує {:.2f} грн".format(price)) # Округлення до двох знаків після точки
print("До ціни додалось {:.1%}".format(increase)) # Виводе відсоток до одного числа після точки
print("На складі {:.0e} деталей".format(details_sum)) # E форма представлення чисел