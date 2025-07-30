# Описуємо клас
class User: 
    # статичні атрібути
    user_name = "Admin"
    password = "qwerty"
    is_banned = False
    friends = []
    
    # Конструктор класа
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    # Методи класа
    def print_info(self):
        print(" Name: {}\n Passowrd: {} \n Ban status: {}".format(
            self.user_name,
            self.password,
            self.is_banned
        ))
    
    def add_friend(self, friend):
        self.friends.append(friend) 
        
user1 = User("Bob", 10000)

user1.print_info()

# import garden - імпортуємо клас з його методами, звертання до методу іде через garden.METHOD()
# from garden import * - імпортуємо всі методи з класу тоді можна на пряму звертатись до методу
# from garden import { METHOD } - імпортуємо тільки ті методи з класу які потрібні

# Якщо необхідно зробити початок реалізації програми та тестувати
class One:
    pass  # Вказуємо для пропуску щоб не заважало виконанню коду
    
class Two:
    def __add__(self, other):
        if isinstance(other, One): # Перевірка чи належить властивість до іншого класу
            print(other)
    
class Three:
    pass

class Four:
    pass