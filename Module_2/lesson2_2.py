def phone(model: str, charge: int = 10, storage: str = "128 Gb", status: str = "working") -> None:
    """
    :param model: model phone
    :param charge: percent of charge available
    :param storage: overall storage size
    :param status: system status of phone
    :return: None
    This function display info about phone
    """
    if not 0 <= charge <= 100:
        print("incorrect charge data!")
        return
    print(
        f"This {model} is {charge} percent charged."
        f"It has {storage} of storage, current status is '{status}'."
    )


def phone_2(model: str, charge: int = 10, storage: str = "128 Gb", status: str = "working") -> None:
    """
    :param model: model phone
    :param charge: percent of charge available
    :param storage: overall storage size
    :param status: system status of phone
    :return: None
    This function display info about phone
    """
    if not 0 <= charge <= 100:
        print("incorrect charge data!")
        return
    print(
        f"This {model} is {charge} percent charged."
        f"It has {storage} of storage, current status is '{status}'."
    )


help(phone)
phone('Iphone, phone_1')

phone_copy = phone_2
print(phone_copy("CopyPhone"))

l_func = lambda x: 2 ** x
print(f"l_func =", l_func)


def func(x):
    return 2 ** x


a = [1, 2, 3, 4, 5]
b = sorted(a, key=lambda x: -x)
print(b)


def order(x):
    return -x


b = sorted(a, key=order)
print(b)


# рекурсивный вызов функции
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# нерекурсивное решение вычисления факториала
def factorial_2(n):
    result = 1
    for i in range(n, 1, -1):
        result += 1
    return result


print(f"{factorial_2(5)} factorial 2")