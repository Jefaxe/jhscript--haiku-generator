#import statements
import easygui
import os
import random
import sys

def main():
    #create list of first-liners
    haiku_list = os.listdir("haikus/poems")
    
    poem = random.choice(haiku_list)
    with open("haikus/poems/"+poem) as haiku_line: #for line one
        line_1 = haiku_line.readlines()[0]

    poem = random.choice(haiku_list)
    with open("haikus/poems/"+poem) as haiku_line: #for line one
        line_2 = haiku_line.readlines()[1]

    poem = random.choice(haiku_list)
    with open("haikus/poems/"+poem) as haiku_line: #for line one
        line_3 = haiku_line.readlines()[2]

    generated_haiku = line_1+line_2+line_3
    option=easygui.buttonbox(generated_haiku,"Haiku Generater",["Save","Don't Save"])
    if option=="Save":
            valid=False
            while not valid:
                filename=easygui.enterbox("What do you want to save the file as?")+".txt"
                if filename in os.listdir("haikus/exports"):
                    easygui.msgbox("There is already an exported poem with that name")
                else:
                    valid=True
            with open("haikus/exports/"+filename,"w") as savehaiku:
                savehaiku.write(generated_haiku)
    elif option==None:
        sys.exit(0)


if __name__=="__main__":
    while True:
        main()
