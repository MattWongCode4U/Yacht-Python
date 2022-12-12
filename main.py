from tkinter import *
from die import *
from yacht import *

root = Tk()
root.title("Yacht Dice Game")
root.iconbitmap("images/MW.ico")

DiceArr = [Die(), Die(), Die(), Die(), Die()]
aRoll = IntVar()
bRoll = IntVar()
cRoll = IntVar()
dRoll = IntVar()
eRoll = IntVar()
y = yacht()
y.populateDict(DiceArr)

# Display UI of game
def UI():
    y.populateDict(DiceArr)

    r = 0
    title = Label(root, text="Yacht Dice Game").grid(row=r, column=0, columnspan=5)

    # Categories
    # Ones
    r += 1
    Label(root, text="Ones: ").grid(row=r, column=0)
    onesBtn = Button(root, text="Score Ones",
                     command=lambda: [y.resetRerolls(), y.scoreOnes(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.ones == -1:
        ones = Label(root, text=str(y.onesCalc(DiceArr)), fg="red")
    else:
        ones = Label(root, text=str(y.ones), fg="green")
        onesBtn["state"] = DISABLED
    ones.grid(row=r, column=1)
    onesBtn.grid(row=r, column=2)

    # Twos
    r += 1
    Label(root, text="Twos: ").grid(row=r, column=0)
    twosBtn = Button(root, text="Score Twos",
                     command=lambda: [y.resetRerolls(), y.scoreTwos(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.twos == -1:
        twos = Label(root, text=str(y.twosCalc(DiceArr)), fg="red")
    else:
        twos = Label(root, text=str(y.twos), fg="green")
        twosBtn["state"] = DISABLED
    twos.grid(row=r, column=1)
    twosBtn.grid(row=r, column=2)

    # Threes
    r += 1
    Label(root, text="Threes: ").grid(row=r, column=0)
    threesBtn = Button(root, text="Score Threes",
                       command=lambda: [y.resetRerolls(), y.scoreThrees(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.threes == -1:
        threes = Label(root, text=str(y.threesCalc(DiceArr)), fg="red")
    else:
        threes = Label(root, text=str(y.threes), fg="green")
        threesBtn["state"] = DISABLED
    threes.grid(row=r, column=1)
    threesBtn.grid(row=r, column=2)

    # Fours
    r += 1
    Label(root, text="Fours: ").grid(row=r, column=0)
    foursBtn = Button(root, text="Score Fours",
                      command=lambda: [y.resetRerolls(), y.scoreFours(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.fours == -1:
        fours = Label(root, text=str(y.foursCalc(DiceArr)), fg="red")
    else:
        fours = Label(root, text=str(y.fours), fg="green")
        foursBtn["state"] = DISABLED
    fours.grid(row=r, column=1)
    foursBtn.grid(row=r, column=2)

    # Fives
    r += 1
    Label(root, text="Fives: ").grid(row=r, column=0)
    fivesBtn = Button(root, text="Score Fives",
                      command=lambda: [y.resetRerolls(), y.scoreFives(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.fives == -1:
        fives = Label(root, text=str(y.fivesCalc(DiceArr)), fg="red")
    else:
        fives = Label(root, text=str(y.fives), fg="green")
        fivesBtn["state"] = DISABLED
    fives.grid(row=r, column=1)
    fivesBtn.grid(row=r, column=2)

    # Sixes
    r += 1
    Label(root, text="Sixes: ").grid(row=r, column=0)
    sixesBtn = Button(root, text="Score Sixes",
                      command=lambda: [y.resetRerolls(), y.scoreSixes(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.sixes == -1:
        sixes = Label(root, text=str(y.sixesCalc(DiceArr)), fg="red")
    else:
        sixes = Label(root, text=str(y.sixes), fg="green")
        sixesBtn["state"] = DISABLED
    sixes.grid(row=r, column=1)
    sixesBtn.grid(row=r, column=2)

    # Full House
    r += 1
    Label(root, text="Full House: ").grid(row=r, column=0)
    fullHouseBtn = Button(root, text="Score Full House",
                          command=lambda: [y.resetRerolls(), y.scoreFullHouse(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.fullHouse == -1:
        fullHouse = Label(root, text=str(y.fullHouseCalc(DiceArr)), fg="red")
    else:
        fullHouse = Label(root, text=str(y.fullHouse), fg="green")
        fullHouseBtn["state"] = DISABLED
    fullHouse.grid(row=r, column=1)
    fullHouseBtn.grid(row=r, column=2)

    # Four of a kind
    r += 1
    Label(root, text="Four of a Kind: ").grid(row=r, column=0)
    fourOfAKindBtn = Button(root, text="Score Four of a Kind",
                            command=lambda: [y.resetRerolls(), y.scorefourOfAKind(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.fourOfAKind == -1:
        fourOfAKind = Label(root, text=str(y.fourOfAKindCalc(DiceArr)), fg="red")
    else:
        fourOfAKind = Label(root, text=str(y.fourOfAKind), fg="green")
        fourOfAKindBtn["state"] = DISABLED
    fourOfAKind.grid(row=r, column=1)
    fourOfAKindBtn.grid(row=r, column=2)

    # Little Straight
    r += 1
    Label(root, text="Little Straight: ").grid(row=r, column=0)
    littleStraightBtn = Button(root, text="Score Little Straight",
                               command=lambda: [y.resetRerolls(), y.scoreLittleStraight(DiceArr), y.rerollAll(DiceArr),
                                                UI()])

    if y.littleStraight == -1:
        littleStraight = Label(root, text=str(y.littleStraightCalc(DiceArr)), fg="red")
    else:
        littleStraight = Label(root, text=str(y.littleStraight), fg="green")
        littleStraightBtn["state"] = DISABLED
    littleStraight.grid(row=r, column=1)
    littleStraightBtn.grid(row=r, column=2)

    # Big Straight
    r += 1
    Label(root, text="Big Straight: ").grid(row=r, column=0)
    bigStraightBtn = Button(root, text="Score Big Straight",
                            command=lambda: [y.resetRerolls(), y.scoreBigStraight(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.bigStraight == -1:
        bigStraight = Label(root, text=str(y.bigStraightCalc(DiceArr)), fg="red")
    else:
        bigStraight = Label(root, text=str(y.bigStraight), fg="green")
        bigStraightBtn["state"] = DISABLED
    bigStraight.grid(row=r, column=1)
    bigStraightBtn.grid(row=r, column=2)

    # Choice
    r += 1
    Label(root, text="Choice: ").grid(row=r, column=0)
    choiceBtn = Button(root, text="Score Choice",
                       command=lambda: [y.resetRerolls(), y.scoreChoice(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.choice == -1:
        choice = Label(root, text=str(y.choiceCalc(DiceArr)), fg="red")
    else:
        choice = Label(root, text=str(y.choice), fg="green")
        choiceBtn["state"] = DISABLED
    choice.grid(row=r, column=1)
    choiceBtn.grid(row=r, column=2)

    # Yacht
    r += 1
    Label(root, text="Yacht: ").grid(row=r, column=0)
    yachtBtn = Button(root, text="Score Yacht",
                      command=lambda: [y.resetRerolls(), y.scoreYacht(DiceArr), y.rerollAll(DiceArr), UI()])

    if y.yacht == -1:
        yacht = Label(root, text=str(y.yachtCalc(DiceArr)), fg="red")
    else:
        yacht = Label(root, text=str(y.yacht), fg="green")
        yachtBtn["state"] = DISABLED
    yacht.grid(row=r, column=1)
    yachtBtn.grid(row=r, column=2)

    # Total
    r += 1
    y.totalCalc()
    Label(root, text="Total: ").grid(row=r, column=0)
    Label(root, text=str(y.total), fg="green").grid(row=r, column=1)

    # Dice Values
    r += 1
    Label(root, text="A").grid(row=r, column=0)
    Label(root, text="B").grid(row=r, column=1)
    Label(root, text="C").grid(row=r, column=2)
    Label(root, text="D").grid(row=r, column=3)
    Label(root, text="E").grid(row=r, column=4)
    r += 1
    Label(root, text=str(DiceArr[0].value)).grid(row=r, column=0)
    Label(root, text=str(DiceArr[1].value)).grid(row=r, column=1)
    Label(root, text=str(DiceArr[2].value)).grid(row=r, column=2)
    Label(root, text=str(DiceArr[3].value)).grid(row=r, column=3)
    Label(root, text=str(DiceArr[4].value)).grid(row=r, column=4)

    # Checkboxes and labels
    r+=1
    Checkbutton(root, text="A", width=10, variable=aRoll).grid(row=r, column=0)
    Checkbutton(root, text="B", width=10, variable=bRoll).grid(row=r, column=1)
    Checkbutton(root, text="C", width=10, variable=cRoll).grid(row=r, column=2)
    Checkbutton(root, text="D", width=10, variable=dRoll).grid(row=r, column=3)
    Checkbutton(root, text="E", width=10, variable=eRoll).grid(row=r, column=4)

    # Reroll Button
    r += 1
    if y.rerollCount <= 0:
        rerollBtn = Button(root, text="Reroll Selected x" + str(y.rerollCount), padx=50, state=DISABLED)
    else:
        rerollBtn = Button(root, text="Reroll Selected x" + str(y.rerollCount), padx=50, command=lambda: rerollClick(y))
    rerollBtn.grid(row=r, column=0)

    # Restart Game Button
    Button(root, text="Restart Game", padx=50, command=lambda: [y.resetGame(DiceArr), UI()]).grid(row=r, column=1)

# Refresh UI and reroll selected dice
def rerollClick(y):
    y.rerollCount -= 1
    if aRoll.get() == 1:
        DiceArr[0].reroll()
    if bRoll.get() == 1:
        DiceArr[1].reroll()
    if cRoll.get() == 1:
        DiceArr[2].reroll()
    if dRoll.get() == 1:
        DiceArr[3].reroll()
    if eRoll.get() == 1:
        DiceArr[4].reroll()
    UI()


UI()
root.mainloop()
