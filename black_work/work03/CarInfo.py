from math import fabs  # 未使用的导入，可考虑移除以保持代码整洁


class CarInfo:
    """车辆信息类，封装车辆基本属性与引擎启停逻辑"""

    def __init__(self, name: str, branch: str, price: float):
        """
        初始化车辆实例
        Args:
            name:   车型名称
            branch: 品牌/车系
            price:  车辆价格（单位：元）
        """
        self.name = name
        self.branch = branch
        self.price = price
        self.engine = None  # 引擎状态：None 表示未初始化，非 None 表示已配置

    def init_engine(self, engine: tuple[int, int, int]) -> None:
        """
        配置引擎参数
        Args:
            engine: 三元组，分别代表引擎的（排量_cc, 马力_ps, 扭矩_Nm）
        """
        self.engine = engine

    def do_running(self) -> bool:
        """启动车辆：引擎已配置时方可运行，否则静默失败"""
        ret = self.engine is not None
        print(f"{self.name} do_running:{ret}")
        return ret

    def do_stop(self) -> bool:
        """停止车辆：引擎未配置视为已停止，不允许在无引擎状态下执行停止操作"""
        ret = self.engine is None
        print(f"{self.name} do_stop:{ret}")
        return ret


def car_info_work() -> None:
    """演示 CarInfo 类的完整使用流程：创建 → 配置引擎 → 启动"""
    car_info = CarInfo("ae86", "toyota", 34000)
    car_info.init_engine((80, 80, 80))  # 配置引擎参数（排量/马力/扭矩）
    car_info.do_running()


if __name__ == "__main__":
    car_info_work()
