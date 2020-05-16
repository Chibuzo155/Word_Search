import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter 'Y' if Yes, or 'N' if No: " % get_close_matches(word, data.keys())[0])
        if ans == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif ans == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "This option is not valid."
    else:
        return "The word doesn't exist. Please check again."

word = input("Enter desired word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
