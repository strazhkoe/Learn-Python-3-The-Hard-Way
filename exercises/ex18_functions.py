def print_two(*args):
    arg1, arg2 = args
    print(f"print_two: {arg1}, {arg2}")

def print_two_fixed_args(arg1, arg2):
    print(f"print_two_fixed_args: {arg1}, {arg2}")

def print_one(arg):
    print(f"print_one: {arg}")

def print_none():
    print("print_none")

print_two("Hello", "world")
print_two_fixed_args("First", "Second")
print_one("One arg")
print_none()