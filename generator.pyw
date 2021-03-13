try:
    import easygui
except ModuleNotFoundError:
    print("Remember to run setup.bat (Windows) or setup.sh (Unix: Mac/Linux)")

import json
import random
import sys

def main():
    with open("haikus/data/words.json") as words:
        words=json.load(words)

    pronounType =  random.choice(list(words["pronouns"].keys()))
    pronoun = random.choice(words["pronouns"][pronounType])
    if pronounType=="+s":
        newAdjectives=[]
        for x in words["adjectives"]:
            x+="s"
            newAdjectives.append(x)
        words["adjectives"]=newAdjectives
    adjective = random.choice(words["adjectives"])
    noun = random.choice(words["nouns"])

    check=easygui.msgbox([pronoun,adjective,noun])
    if check == None:
        sys.exit(1)

if __name__=="__main__":
    while True:
        main()
