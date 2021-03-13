#call this in your setup.bat /setup.sh / some setup file. Or call it from your project directly (it slows down the start-up, do not use forceUpdate=True)
import urllib.request
import os
import shutil
import sys

def run(forceUpdate=False):
    if not os.path.exists("libs/jeflib.py") and not forceUpdate:
        if not os.path.exists("libs"):
            os.mkdir("libs")
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jeflib/main/jeflib.py") as response, open("libs/jeflib.py", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    elif forceUpdate:
        if not os.path.exists("libs"):
            os.mkdir("libs")
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen("https://raw.githubusercontent.com/Jefaxe/jeflib/main/jeflib.py") as response, open("libs/jeflib.py", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

            
if __name__=="__main__":
    try:
        run()
    except urllib.error.URLError:
        print("NO INTERNET, NOT UPDATING")
        sys.exit(1)
