# True False пишутся з великої букви
# Приклад використання while за умови співпадіння
password = int(input("Enter password: "))

while password != 235:
    
    print("Wrong password!")
    password = int(input("Try again: "))

print("Password correct, welcome!") 

# Приклад використання while за умови якщо менше
balance = int(input("Enter your balance: "))

while balance > 5000:

    product_cost = int(input("Enter cost product: "))
    balance -= product_cost

print("Your balanc is less 5000")

# Преривання цикла
weather = int(input("Enter how many degrees: "))
meters = 0 

while weather > 15:

    meters += 20
    weather -= 2

    if weather <= 15:
        break

    meters += 10

print("Meters passed", meters)

# Пропуск ітерації
number = int(input("Enter your number: "))

while number >= 0:

    if number == 3:
        nember -= 1
        continue

    print (number)
    number -= 1