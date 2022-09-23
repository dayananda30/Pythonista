def multiply(num1: str, num2: str) -> str:
    n1 = get_number(num1)
    n2 = get_number(num2)
    return str(n1 * n2)


def get_number(num):
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = 0
    for digit in num:
        result = 10 * result + value[digit]
    return result
