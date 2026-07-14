from black_work.work02 import utils


def my_main():
    print("hello")
    a: int = 5
    b: int = 6
    utils.do_add(a, b)
    utils.do_sub(a, b)
    print(f"add:{utils.do_add(a, b)},sub:{utils.do_sub(a, b)},time:{utils.do_time(a, b)},divide:{utils.do_div(a, b)}")


if __name__ == "__main__":
    my_main()
