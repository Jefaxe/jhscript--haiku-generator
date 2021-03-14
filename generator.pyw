#import statements
import easygui
import os
import random
import sys
import urllib.request
import libs.jeflib as jb
import threading

def downloadHaikus():
    if jb.connected():
        max_number = urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jhscript--haiku-generator/main/haikus/maxPoems.txt")
        for x in range(1,int(max_number.read())+1):
            if not os.path.exists("haikus/poems/haiku-"+str(x)):
                jb.downloadFile("https://raw.githubusercontent.com/Jefaxe/jhscript--haiku-generator/main/haikus/poems/haiku-"+str(x)+".txt","haikus/poems/haiku-"+str(x)+".txt")
def main():
    #create list of first-liners
    def getHaikuList():
        haiku_list = os.listdir("haikus/poems")
        try:
            haiku_list.remove(".DS_Store") #mac finder folder configeration file. Always present on MACOSX.
        except ValueError:
            pass  
        try:
            haiku_list.remove("desktop.ini") #windows folder configeration file. Only present if you make changes to the folder settings. Windows only.
        except ValueError:
            pass
        return haiku_list
    haiku_list=getHaikuList()
    try:
        poem = random.choice(haiku_list)
    except IndexError:
        downloadHaikus()
        haiku_list=getHaikuList()
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
