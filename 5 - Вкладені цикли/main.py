# Вкладений цикл приклад
for a in range(1, 10):
    for b in range(1, 10):
        print(a, "*", b, "=", a * b)

# Умовний оператор всередені цикла
for row in range(20):
    for col in range(50):
        if row == 9:
            print("-", end = "")
        elif col == 24: 
            print("|", end = "")
        else: 
            print(" ", end = "")
    print()

# Блок else у циклі
for attempt in range(1, 4):
    pincode = int(input("Enter your pin-code: "))
    if pincode == 1234:
        print("Success? get yor money")
        break
    print("Pin-code is wrong, try again, count attempt - ", 3 - attempt)
else: 
    print("Your card is blocked, good bye")