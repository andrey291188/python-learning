# Рекусія
def factorial(num):
    if(num == 1):
        return 1
    fact_n_minus_1 = factorial(num - 1)
    return num * fact_n_minus_1

num_fact = factorial(5)
print(num_fact)

# Ще приклад рекурсії по словарю
site = {
    "html": {
        "head": {
            "title": "My site"
        },
        "body": {
            "h2": "This is title on site",
            "div": "This is block some on site",
            "p": "Whis is decription on site"
            }
        }
    }

def find_key(struct, key):
    
    if key in struct: 
        return struct[key]
    
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result: 
                break
    else:
        result = None
    
    return result

user_key = input("Enter the key: ")
value = find_key(site, user_key)

if value: 
    print(value)
else:
    print("That key not in structure")

# Ще приклад рекурсій створення масиву з числами  
def create_array(n):
    if n == 0:
        return []
    else:
        return create_array(n - 1) + [n]

print(create_array(5))

# Передача аргументів в функцію та встановлення по замовчуванню
def myFunc(value1, value2="Значення по замовчуванню", value3=3):
    print(value1, value2, value3)

myFunc("Question 1", "Question2", 4)
myFunc("Question 1")
myFunc("Question 1", "Question2")
myFunc("Question 1", value3=4)

# Збираємо аргументи в функції
def func(first_args, *args, **kwargs):
    print("First args", first_args)
    print("Second args", args)
    print("Third args", kwargs)
  
func(20, 1000, 2000, 3000, 250, 1980, year=1998, doc_type="report", operation_id=123123123)