def execute(func, *args):
    return func(*args)

def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

# Gọi thử hàm
execute(say_hello, "Peter", "George")  # Output: Hello, Peter, I am George
execute(say_bye, "Peter")  # Output: Bye, Peter
