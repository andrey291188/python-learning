# Ітератор
items = [10, 20, 30]

iterator = iter(items) # Додаємо список в ітератор 

next(iterator) # Виводимо по одному елементу

# Ліниві обчислення
class Fibonacci:
    
    def __init__(self, number):
        
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number
    
    def __iter__(self):
        
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        
        return self
    
    def __next__(self):
        
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration()
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
            
        return self.cur_val
    
fib_iterator = Fibonacci(10)

print(8 in fib_iterator) # lazy evaluation

# Генератор
def fibonacci(number):
    cur_val = 0
    next_val = 1
    
    for _ in range(number):
        yield cur_val # Замороження функції
        cur_val, next_val = next_val, cur_val + next_val
        
fib_seq = fibonacci(number=10)
for i_val in fib_seq:
    print(i_val)

# Генератор від генератора
def square(nums):
    for num in nums:
        yield num ** 2
    
print(sum(square(fibonacci(number=50000))))

# Генераторний вираз
cubes_gen = (num ** 3 for num in range(10))
for i_num in cubes_gen:
    print(i_num, end=' ')
    
# Аннотациї типів
class Person:
    def __init__(self, name: str, age: int, friend: list) -> None: # Опис типів даних які приймає та повертає функція
        self.__name = name
        self.__age = age
        self.__friends = friend
    
    def __str__(self) -> None:
        return "Name: {}\t Age: {}\t Friends: {}". format(
            self.__name, self.__age, self.__friends
        )
        
    def set_age(self, age: int) -> None:
        self.__age = age
        
    def get_age(self) -> int:
        return self.__age
    
