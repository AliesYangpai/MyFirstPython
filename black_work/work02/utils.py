def do_add(a: int, b: int) -> int:
    return a + b


def do_sub(a: int, b: int) -> int:
    return a - b


def do_div(a: int, b: int) -> float:
    if b == 0:
        return 0
    else:
        return round(a / b,3)


def do_time(a: int, b: int) -> int:
    return a * b
