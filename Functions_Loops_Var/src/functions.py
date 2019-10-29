def some_function():
    print("Hello!")


def function_with_args(name, text):
    print(text + " " + name)


some_function()
function_with_args("Oleg", "Hello")
function_with_args(name="Oleg", text="Hello")
function_with_args(text="Hello", name="OLEG")

#######################################################


def my_sum(a, b):
    return a + b


# prints 21
c = my_sum(10, 11)
print(c)

# prints 21.0
c = my_sum(10.0, 11)
print(c)

#######################################################

global_var = 10


def get_var():
    global_var = 5
    return global_var


# 10
print(global_var)
# 5
print(get_var())
# 10
print(global_var)