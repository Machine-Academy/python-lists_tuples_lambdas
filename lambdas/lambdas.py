# convert the functions below into Lambda / Anonymous functions


def myFunction():
    print("My function was ran!")


myFunction()


def myOtherFunction(param):
    return param


result = myOtherFunction("Testing")
print(result)


def sum_two_nums(num1, num2):
    return num1 + num2


result = sum_two_nums(1, 2)
print(result)


def subtract_two_nums(x, y):
    return x - y


result = subtract_two_nums(4, 2)
print(result)


# Extra
nums_list = [1, 2, 3, 4]


def tripple_num(num):
    return num * 3


tripple = map(tripple_num, nums_list)
print(list(tripple))
