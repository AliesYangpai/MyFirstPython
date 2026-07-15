from math import fabs


class CarInfo:
    def __init__(self, name: str, branch: str, price: float):
        self.name = name
        self.branch = branch
        self.price = price
        self.engine = None

    def init_engine(self, engine: tuple[int, int, int]) -> None:
        self.engine = engine

    def do_running(self) -> bool:
        ret = self.engine is not None
        print(f"{self.name} do_running:{ret}")
        return ret

    def do_stop(self) -> bool:
        ret = self.engine is None
        print(f"{self.name} do_stop:{ret}")
        return ret


def car_info_work() -> None:
    car_info = CarInfo("ae86", "toyota", 34000)
    car_info.init_engine((80, 80, 80))
    car_info.do_running()


if __name__ == "__main__":
    car_info_work()
