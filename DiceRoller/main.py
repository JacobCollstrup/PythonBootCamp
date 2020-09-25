# Main Program
from Dice import DiceRoll

Condition = "y"

while Condition == "y":
    type = int(input("What type of dice do you want to roll? (Input whole number larger than 0.): "))
    number = int(input("How many times do you want to roll it? (Input whole number larger than 0.):"))
    dice_rolls = DiceRoll(type, number)

    print("Your rolls are...")
    print("Roll : Count")

    for roll, count in dice_rolls.items():
        print(roll, " : ", count)

    Condition = input("Press 'y' to continue and roll again, press any key to stop.")