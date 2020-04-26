import json
from difflib import get_close_matches

data = json.load(open("tesla\\pyLearnMegaCourse\\word_search\\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        input_value = input("Did you mean %s instead? Enter Y if yes,or N if no: " % get_close_matches(w,data.keys())[0])
        if input_value == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif input_value == "N":
            return "The word doesn't exist, please double check it."
        else:
            return "We didn't understand your input entry. try the valid input."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the input word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

