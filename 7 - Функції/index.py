import math

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

# Пошук загального найбільшого ділителя
def gcd(a,b):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    print("Найдільший дільник:", a + b)

gcd(30, 20)

print(math.gcd(30, 20))

# Повернення значення з функції
def func(number):
    number * 2
    return number
    
new_number = func(2)
print(new_number)
