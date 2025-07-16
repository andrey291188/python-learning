# Оголошення функції та її виклик 
def countFood():
    fruits = int(input("Введіть кількість фруктів: "))
    vegetables = int(input("Введіть кількість овочей: "))
    print("Всього: ", fruits + vegetables)

print("Мавпи")
countFood()

print("Жирафи")
countFood()

print("Слони")
countFood()

# Аргументи (параметри) в функції
def myAdress(name):
    print(name, "живе за адресою...")

myAdress("Andrii")

# Декілька аргументів (параметрів) в функції
def myAdress(name, house_number):
    print(name, "живе за адресою...,", "будинок номер", house_number)

myAdress("Andrii", 32)