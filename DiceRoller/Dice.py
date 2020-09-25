from random import randint


def DiceRoll(type: int, number: int):
    raw_dice_rolls = []
    for i in range(1, number + 1):
        raw_dice_rolls.append(randint(1, type))

    dice_keys = list(range(1, type + 1))
    dice_rolls = {}

    for roll in dice_keys:
        dice_rolls[roll] = raw_dice_rolls.count(roll)

    return dice_rolls

