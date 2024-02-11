def sum_number(number: int) -> int:
    """
    Повертає суму цілих чисел від нуля до number, якщо number - додатне ціле число, інакше повертає 0.

    >>> sum_number(5)
    15
    >>> sum_number(5.3)
    0
    >>> sum_number(-5)
    0
    >>> sum_number("5")
    0
    """
    try:
        result = sum(range(number + 1))
    except TypeError:
        result = 0
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(sum_number(10))
