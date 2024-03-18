
class Coperative:
    def __init__(self) -> None:
        self.points = 0

    def take_action(self):
        return 1  # 1 means Cooperate


class Cheater:
    def __init__(self) -> None:
        self.points = 0

    def take_action(self):
        return 0  # 0 means cheat