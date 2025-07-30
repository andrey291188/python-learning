# Інкапсюляция сховання даних
class Person: 
    """
    Базовий клас, описує основні методи 
    """ # Опис класа документація докстрінг
    
    __count = 0 # Приватний метод властивості
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        Person.__count += 1 # Звернення до приватного методу властивості
        
    def get_count(self):
        return self.__count # Звертаємось до методу щоб отримати значення приватої властивості
    
    def set_count(self, count): # Встановлення значення для приватної властивості
        if count in range(1, 90): # Перевірка діапазону передаваємого значення
            self.__count = count
        else:
            raise Exception("Wrong value")
        
print(Person._Person__count) # Примусово вивести приватні дані

# Спадковіст в ООП
class Pet: 
    legs = 4
    has_tail = True
     
    def __str__(self):
        tail = "Так" if self.has_tail else "Ні"
        return "Всього ніг: {legs}\n Хвіст присутній - {has_tail}".format(
            legs = self.legs,
            has_tail = tail
        )
        
    def walk (self):
        print("На прогулці")

class Cat(Pet):
    
    def sound(self):
        print("Мяу!")
        
class Dog(Pet):
    
    def sound(self):
        print("Гав!")
        
class Frog(Pet):
    has_tail = False # Зміна базового значення батьківського класу
    
    def sound(self):
        print("Ква!")
        
    def walk (self): # Поліморфізм, змінюємо метод класу
        print("На плавані")
        
# Спадковість ініціалізованих даних
class Ship:
    
    def __init__(self, model):
        self.__model = model
        
class WarShip(Ship):
    
    def __init__(self, model, gun):
        super().__init__(model) # Спадоковість від класу Ship
        self.gun = gun
        
