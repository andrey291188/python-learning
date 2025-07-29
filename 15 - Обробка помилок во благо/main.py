# try та exept для обробки помилок
try:
    
    print("Основний блок виконання коду")
    
    if 1 == 1: 
        raise BaseException("Це виключення яке зупиняє роботу програми")
    
except FileNotFoundError: # Також можна передати кортедж помилок (FileNotFoundError, ValueError) якщо обробка помилок однакова
    
    print("Невірний тип файлу")

except ValueError:
    
    print("Невірний тип даних")

else: 
    
    print("Виконається тоді коли не буде ніяких помилок")
    
finally:
    
    print("Завжди виконається")