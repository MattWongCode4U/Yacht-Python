import random


def roll():
    return random.randint(1, 6)


class Die:
    def __init__(self):
        self.value = roll()

    # initializer for testing with values
    #def __init__(self, num):
    #    self.value = num

    def reroll(self):
        self.value = roll()