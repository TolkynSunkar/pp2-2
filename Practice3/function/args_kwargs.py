def show_numbers(*args):
    for num in args:
        print(num)

show_numbers(1, 2, 3)

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Tolkyn", age=20)