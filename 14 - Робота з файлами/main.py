import os
import zipfile

# Формування шляху в незалежності від системи
folder_name = "project"
file_name = "my_file.txt"

rel_path = os.path.join('docs', folder_name, file_name) # підставляєммо значення для генерації шляху

abs_path = os.path.abspath(file_name) # знайде абсолютний шлях файлу де б він не був

# os.path.abspath("new_folder") Знайде папку в глибині
# os.path.abspath(os.path.join("..", "new_folder")) Знайде папку на рівень вище від тієї яка в глибині
# os.path.abspath("/new_folder") Знайде папку на диску C:\new_folder
# os.path.abspath(os.path.join(os.sep, "/new_folder")) Знайде папку на диску C:\new_folder

# os.listdir(abs_path) Виведе список всьогощо всередені папки

# os.path.exists(abs_path) Повертає True якщо такий каталог існує або False якщо ні
# os.path.isdir(abs_path) Повертає True якщо це каталог або False якщо ні
# os.path.isfile(abs_path) Повертає True якщо це файл або False якщо ні

print(rel_path)

# Читаємо файл
speakers_file = open("speakers.txt", "r", encoding="utf-8")

data = speakers_file.read() # Читаємо файл через метод

for i_line in speakers_file: # Читаємо файл через ітерації
    print(i_line, end="")

print(data)

speakers_file.close # Не забуваємо після роботи закрити файл

# Записуємо в файл дані 
sym_count = ["12\n", "14\n", "15\n", "16\n"] # Масив даних строк для запису

counts_file = open("sym_count.txt", "w") # Створюємо файл, буде переписувати файл, щоб дописувало потрибно замість "w" вказати "a"
counts_file.write(sym_count) # Записуємо дані

counts_file.close # Закриваємо файл 

# data = speakers_file.read(10) в read передаємо кількість символів яку необхідно прочитати

# Функція розпакування архіва
def unzip(file):
    
    zfile = zipfile.ZipFile(file, "r")
    
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
        
    zfile.close

# Безпечне відкриття файлу у випадку падіння програми файл закриєтся
with open("speakers.txt", "r", encoding="utf-8") as speakers:
    
    for i_line in speakers: 
        print(i_line, end="")