def sum_number(number):
    try:
        result = sum(range(number + 1))
    except TypeError:
        result = 0
    return result


if __name__ == "__main__":
    print(sum_number(10))
