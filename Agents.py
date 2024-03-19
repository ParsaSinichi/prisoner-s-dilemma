import numpy as np


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


class Random:
    def __init__(self) -> None:
        self.points = 0

    def take_action(self):
        if np.random.rand() > 0.5:
            return 1
        else:
            return 0


class CopyCat:
    def __init__(self) -> None:
        self.points = 0
        self.memory = []

    def take_action(self):
        if len(self.memory) == 0:

            return 1  # always Cooperates at first
        elif (self.memory[-1] == 0):
            return 0
        else:
            return 1


class CopyKitten:
    """"
    Cooperates at first, only cheats if enemy cheats tow times in a row
    """

    def __init__(self) -> None:
        self.points = 0
        self.memory = []

    def take_action(self):
        if len(self.memory) == 0:
            return 1  # cooperates at first
        if len(self.memory) > 1:
            if self.memory[-1] == 0 and self.memory[-2] == 0:
                return 0  # the enemy didn't coperated two times in a row
            else:
                return 1
        else:
            return 1
