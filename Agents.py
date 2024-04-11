
import numpy as np
Rand = False

rand_prob = 0.20


class Cooperative:
    def __init__(self, Random_miss=False) -> None:
        self.points = 0
        self.Random_miss = Random_miss

    def take_action(self):
        # 1 means Cooperate  // here we are adding missing chance

        return 1


class Detective:
    """

Starts with: Cooperate, Cheat, Cooperate, Cooperate.
Afterwards, if you ever retaliate with a Cheat, it plays like a Copycat.
Otherwise, it plays like an Always Cheat.
    """

    def __init__(self, Random_miss=False) -> None:
        self.moves = [1, 1, 0, 1]
        self.points = 0
        self.memory = []
        self.alway_cheat = False
        self.Random_miss = Random_miss

    def take_action(self):
        if (len(self.moves) != 0):  # first 4 move
            return self.moves.pop()
        else:
            if (self.alway_cheat == False):
                if self.memory[-1] == 0:
                    self.alway_cheat = True
                    return 0
                # else:
                #     if self.memory[-1] == 0:
                #         return 0
                else:

                    return 1
            if self.alway_cheat:
                return 0


class Grudger:
    """
Starts with Cooperate, and keeps cooperating until you cheat it even once.
Afterwards, it always plays Cheat.
    """

    def __init__(self, Random_miss=False) -> None:
        self.memory = []
        self.points = 0
        self.Random_miss = Random_miss

    def take_action(self):
        if (len(self.memory) == 0):
            return 1
        else:
            if 0 in self.memory:
                return 0
            else:
                return 1


class Cheater:
    def __init__(self, Random_miss=False) -> None:
        self.points = 0
        self.Random_miss = Random_miss

    def take_action(self):
        return 0  # 0 means cheat


class Random:
    def __init__(self, Random_miss=False) -> None:
        self.points = 0
        self.Random_miss = Random_miss

    def take_action(self):
        if np.random.rand() >= 0.5:

            return 1
        else:
            return 0


class CopyCat:
    def __init__(self, Random_miss=False) -> None:
        self.points = 0
        self.memory = []
        self.Random_miss = Random_miss

    def take_action(self):
        if len(self.memory) == 0:
            return 1
        elif self.memory[-1] == 0:
            return 0
        else:
            return 1


class Simpleton:
    """
    Starts with Cooperate.
    Then, if you cooperated in last round, it repeats its last move (even if it was an accident).
    But if you cheated in last round, it switches its last move (even if it was an accident).
    """

    def __init__(self, Random_miss=False) -> None:
        self.points = 0
        self.memory = []  # memory of the opponent
        self.actions = []
        self.Random_miss = Random_miss

    def take_action(self):
        if len(self.memory) == 0:
            self.actions.append(1)
            return 1
        else:

            if self.memory[-1] == 1:
                self.actions.append(self.actions[-1])
                return self.actions[-2] if np.random.rand() >= rand_prob else 0
            else:
                self.actions.append(int(not self.actions[-1]))
                return int(not (self.actions[-2]))
            # else:
            #     if self.memory[-1] == 1:
            #         self.actions.append(self.actions[-1])
            #         return self.actions[-2]
            #     else:
            #         self.actions.append(int(not self.actions[-1]))
            #         return int(not (self.actions[-2])) if np.random.rand() >= rand_prob else 0


class CopyKitten:
    """"
    Cooperates at first, only cheats if enemy cheats two times in a row
    """

    def __init__(self, Random_miss=False) -> None:
        self.points = 0
        self.memory = []
        self.Random_miss = Random_miss

    def take_action(self):
        if len(self.memory) == 0:
            return 1  # cooperates at first
        if len(self.memory) > 1:
            if self.memory[-1] == 0 and self.memory[-2] == 0:
                return 0  # the enemy didn't cooperate two times in a row
            else:
                return 1
        else:
            return 1
