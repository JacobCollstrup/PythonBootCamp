import json
from difflib import get_close_matches

def dict_search(input: str):
    with open("data2.json", "r", encoding="utf-8") as dict_file:
        dict = json.load(dict_file)

        keywords = [input, input.lower(), input.upper(), input.title()]


        keywords.extend(get_close_matches(input, dict.keys()))

        result = {}

        for keyword in keywords:
            if keyword in dict:
                result[keyword] = dict[keyword]
            else:
                result[keyword] = ["Word doesn't exist in dictionary! :-("]

    return result