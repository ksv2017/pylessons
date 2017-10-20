import random


def list_of_randomly_generated_ints(range):
    """the description of the function goes here"""
    list = []
    i = 0
    while i < range:
        i += 1
        list.append(random.randint(1,20))
    return list


def convert_celcius_into_farenheit(celcius):
    f = (celcius * 1.8) + 32
    return f


print("My list of randomly generated integers is: ", list_of_randomly_generated_ints(5))

print("The result of conversion from C* to F* is: ", convert_celcius_into_farenheit(10))
