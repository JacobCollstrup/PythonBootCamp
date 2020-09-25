# Main program
from DictionaryData import dict_search


Condition = "y"

while Condition == "y":
    keyword = input("Type in the word you want to look up: ")
    print(f"You searched for '{keyword}':")
    result = dict_search(keyword)

    for key in result:
        for item in result[key]:
            print(f"{key} : {item}")

    Condition = input("Press 'y' to continue and look up another word or press any key to stop.")

