# Цикл for конструкція
winners = 0 

for ticket in 345, 19, 87, 1020, 421, 555:

    if ticket % 5 == 0:
        print("Winner ticket -", ticket)
        winners += 1

print("Count winners -", winners)

# Функція range каже скільки ітерацій потрібно зробити циклу for
text = "Python"

for word_count in range(5):
    print(text)

# Вводимо діапазон чисел з чого почати та де закінчити
start_number = 1
end_number = 6

for number in range(start_number, end_number):
    print(number)

# Вводимо діапазон чисел з шагом, з чого почати та де закінчити та який шог робити
start_number = 1
end_number = 6
step_number = 2 # Також можна використовувати - для відємнго цикла

for number in range(start_number, end_number, step_number):
    print(number)

# Цикл по рядку

phase = input("Enter your phrase: ")

for symbol in phase:
    print(symbol * 5) # символи можемо множити для кількості
    print(symbol, end = " ") # end вказує чим закинчити за замовчуванням \n - перенос строки