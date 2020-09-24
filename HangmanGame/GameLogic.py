from WordBank import HangmanPics
from WordBank import WordBank

global guess_counter

def GameLogic():
    def print_output():
        print()
        print(''.join([x + ' ' for x in output]))

    guess_counter = 0
    word = WordBank()
    space = len(word)
    output = ["_"] * space
#    print(word)
    print("Category is animals.")

    while ["_" in output]:

        print_output()
        guess = input("Guess word or letter: \n")
        if guess == word:
            print("You win!")
            break
        elif guess in word:
            print("Correct", guess)
            #       print("I am in 'elif'-loop...")
            for i, x in enumerate(word):
                #            print("I am in nested for-loop, under elif-loop...")
                if x is guess:
                    #                print("I am in nested if-loop, under the for loop above, testing if input is in the word...")
                    output[i] = guess
            if "_" not in output:
                #            print("I am in nested if-loop, same level as nested for-loop, testing win-condition...")
                print("You win!")
                break
        else:
            #        print("I am in else-loop, testing for wrong guess and updating guess counter...")
            print(HangmanPics(guess_counter))
            guess_counter += 1
            print("Incorrect ", guess)
            if guess_counter > 6:
                #            print("I am in nested if loop, under else-loop, testing loose condition.")
                print("You lose!")
                break
            print(f"You have {7 - guess_counter} guesses remaining.")

