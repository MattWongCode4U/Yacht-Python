import operator

class yacht:
    def __init__(self):
        self.rerollCount = 2
        self.ones = -1
        self.twos = -1
        self.threes = -1
        self.fours = -1
        self.fives = -1
        self.sixes = -1
        self.fullHouse = -1
        self.fourOfAKind = -1
        self.littleStraight = -1
        self.bigStraight = -1
        self.choice = -1
        self.yacht = -1
        self.total = 0

        self.dict = {}

    def populateDict(self, dice):
        self.dict.clear()
        for d in dice:
            self.dict[d.value] = self.dict.get(d.value, 0) + 1

    def resetRerolls(self):
        self.rerollCount = 2

    def rerollAll(self, dice):
        for d in dice:
            d.reroll()

    # Reset game re-initialize and reroll dice
    def resetGame(self, dice):
        self.rerollAll(dice)
        self.__init__()

    # Ones
    def onesCalc(self, dice):
        t = 0
        for d in dice:
            if d.value == 1:
                t += d.value
        return t
    def scoreOnes(self, dice):
        self.ones = self.onesCalc(dice)

    # Twos
    def twosCalc(self, dice):
        t = 0
        for d in dice:
            if d.value == 2:
                t += d.value
        return t
    def scoreTwos(self, dice):
        self.twos = self.twosCalc(dice)

    # Threes
    def threesCalc(self, dice):
        t = 0
        for d in dice:
            if d.value == 3:
                t += d.value
        return t
    def scoreThrees(self, dice):
        self.threes = self.threesCalc(dice)

    # Fours
    def foursCalc(self, dice):
        t = 0
        for d in dice:
            if d.value == 4:
                t += d.value
        return t
    def scoreFours(self, dice):
        self.fours = self.foursCalc(dice)

    # Fives
    def fivesCalc(self, dice):
        t = 0
        for d in dice:
            if d.value == 5:
                t += d.value
        return t
    def scoreFives(self, dice):
        self.fives = self.fivesCalc(dice)

    # Sixes
    def sixesCalc(self, dice):
        t = 0
        for d in dice:
            if d.value == 6:
                t += d.value
        return t
    def scoreSixes(self, dice):
        self.sixes = self.sixesCalc(dice)

    # Full House
    def fullHouseCalc(self, dice):
        threeofakind = False
        pair = False
        for key in self.dict:
            if self.dict[key] == 3:
                threeofakind = True
            if self.dict[key] == 2:
                pair = True
        if threeofakind and pair:
            return self.choiceCalc(dice)
        else:
            return 0
    def scoreFullHouse(self, dice):
        self.fullHouse = self.fullHouseCalc(dice)

    # Four of a Kind
    def fourOfAKindCalc(self, dice):
        fourofakind = False
        score = 0
        for key in self.dict:
            if self.dict[key] == 4:
                fourofakind = True
                score = key * 4
        return score
    def scorefourOfAKind(self, dice):
        self.fourOfAKind = self.fourOfAKindCalc(dice)

    # Little Straight
    def littleStraightCalc(self, dice):
        list = dice[:]
        list = sorted(list, key=operator.attrgetter("value"))
        count = 0

        for i, d in enumerate(list):
            # Check if last item
            if i == len(list) - 1:
                if list[i - 1].value == d.value - 1:
                    count += 1
                break
            # Check if next item is 1 value more
            elif list[i + 1].value == d.value + 1:
                count += 1
                continue
        if count >= 4:
            return 25
        else:
            return 0
    def scoreLittleStraight(self, dice):
        self.littleStraight = self.littleStraightCalc(dice)

    # Big Straight
    def bigStraightCalc(self, dice):
        list = dice[:]
        list = sorted(list, key=operator.attrgetter("value"))
        count = 0

        for i, d in enumerate(list):
            # Check if last item
            if i == len(list) - 1:
                if list[i - 1].value == d.value - 1:
                    count += 1
                break
            # Check if next item is 1 value more
            elif list[i + 1].value == d.value + 1:
                count += 1
                continue
        if count >= 5:
            return 30
        else:
            return 0
    def scoreBigStraight(self, dice):
        self.bigStraight = self.bigStraightCalc(dice)

    # Choice
    def choiceCalc(self, dice):
        temp = 0
        for d in dice:
            temp += d.value
        return temp
    def scoreChoice(self, dice):
        self.choice = self.choiceCalc(dice)

    # Yacht
    def yachtCalc(self, dice):
        dval = dice[0].value
        for d in dice:
            if d.value != dval:
                return 0
        return 50
    def scoreYacht(self, dice):
        self.yacht = self.yachtCalc(dice)

    # Calculate totals
    def totalCalc(self):
        temp = 0
        if self.ones > -1:
            temp += self.ones
        if self.twos > -1:
            temp += self.twos
        if self.threes > -1:
            temp += self.threes
        if self.fours > -1:
            temp += self.fours
        if self.fives > -1:
            temp += self.fives
        if self.sixes > -1:
            temp += self.sixes
        if self.fullHouse > -1:
            temp += self.fullHouse
        if self.fourOfAKind > -1:
            temp += self.fourOfAKind
        if self.littleStraight > -1:
            temp += self.littleStraight
        if self.bigStraight > -1:
            temp += self.bigStraight
        if self.choice > -1:
            temp += self.choice
        if self.yacht > -1:
            temp += self.yacht
        self.total = temp
