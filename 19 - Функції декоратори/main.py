import time
import functools
from typing import Callable, Any, Dict

# Функція декоратор підрахунку часу виконання
def timer(func: Callable) -> Callable:
    
    @functools.wraps(func) # Щоб не губити властивості передаваємої функції.
    def wraped_func(*args, **kwargs)-> Any:
        
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        
        print(run_time)
        
        return result
    
    return wraped_func

# Функція декоратор логування роботи функції
def logging(func: Callable) -> Callable:
    
    def wraped_func(*args, **kwargs)-> Any:
        print("\nWorking function {func}\t" 
              "args {args}\t" 
              "kwargs {kwargs}".format(
                  func=func.__name__, 
                  args=args, 
                  kwargs=kwargs))
        
        result = func(*args, **kwargs)
        print("Function completed successfully")

        return result
    
    return wraped_func

# Функція без аргументів
@timer # Різний порядок виконання функцій декораторів в залежності від їх розташування
@logging
def squares_sum() -> int:
    number = 100
    result = 0
    
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
        
    return result

# Функція з аргументами
@logging # Різний порядок виконання функцій декораторів в залежності від їх розташування
@timer
def cubes_sum(number: int) -> int:   
    result = 0
    
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(10000)])
        
    return result


my_result = squares_sum()
print(my_result)

my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)

# Функція декоратор яка записує в словник виконання функцій
PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name: str) -> str:
    return "Hello {name}".format(name=name)

@register
def say_goodbye(name: str) -> str:
    return "Goodbye {name}".format(name=name)

print(PLUGINS)
print(say_hello("Tom"))
