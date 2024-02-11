def sum_number(number):
    result = 0
    for num in range(number + 1):
        result += num
    return result


if __name__ == "__main__":
    print(sum_number(10))
