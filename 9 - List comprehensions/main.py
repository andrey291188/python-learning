# List comprehensions Представлення списку
squares = [x ** 2 for x in range(10)]

# Приклад роботи з List comprehensions 
def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]

first_percent = int(input("Підвищення цін на перший рік: "))
second_percent = int(input("Підвищення цін на другий рік: "))

price_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
price_second = [get_higher_price(second_percent, i_price) for i_price in price_first]

print(round(sum(prices_now), 2), round(sum(price_first), 2), round(sum(price_second), 2))

# List comprehensions з умовою
squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]

# Дві умови, для одних значень в квадраті да інших в кубі
squares_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]

# Модуль random для генерування випадкових чисел
import random
random_number = random.randint(50, 100)

# Робимо копію списка
nums = [1, 2, 3, 4, 5]
nums2 = nums[:]
nums2[3] = 0

print(nums)  # [1, 2, 3, 4, 5]
print(nums2)  # [1, 2, 3, 0, 5] 

# Зрізи списка
print(nums2[1:3]) # Виводимо зріз списка [2, 3]
print(nums2[:3]) # Виводимо зріз списка [1, 2, 3]
print(nums2[1:]) # Виводимо зріз списка [2, 3, 0, 5]
print(nums2[1:4:2]) # Виводимо зріз списка з шагом [2, 0]
print(nums2[::-1]) # Виводимо зріз списка [5, 0, 3, 2, 1]

# Вкладені списки (розгладження масиву)
nice_list = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[10, 11, 12],[13, 14, 15],[16, 17, 18]]]
#          (     ((    перший список        )    другий список           )      третій список     )   
new_list = [digit for each_list in nice_list for each_list_2 in each_list for digit in each_list_2]