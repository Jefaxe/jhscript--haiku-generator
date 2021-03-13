#import statements
import easygui
import os
import random
import sys
import urllib.request
import libs.jeflib as jb
import argparse
import threading

def downloadHaikus():
    if jb.connected():
        max_number = urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jhscript--haiku-generator/main/haikus/poems/max.txt")
        for x in range(1,int(max_number.read())+1):
            if not os.path.exists("haikus/poems/haiku-"+str(x)):
                jb.downloadFile("https://raw.githubusercontent.com/Jefaxe/jhscript--haiku-generator/main/haikus/poems/haiku-"+str(x)+".txt","haikus/poems/haiku-"+str(x)+".txt")
def main():
    #create list of first-liners
    haiku_list = os.listdir("haikus/poems")
    try:
        poem = random.choice(haiku_list)
    except IndexError:
        downloadHaikus()
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
                filename=easygui.enterbox("What do you want to save the file as?")
                if filename==None:
                    break
                else:
                    filename+=".txt"
                if filename in os.listdir("haikus/exports"):
                    easygui.msgbox("There is already an exported poem with that name")
                else:
                    valid=True
            if valid:
                with open("haikus/exports/"+filename,"w") as savehaiku:
                    savehaiku.write(generated_haiku)
    elif option==None:
        sys.exit(0)


if __name__=="__main__":
    update = threading.Thread(target=downloadHaikus)
    update.start()
    while True:
        main()
