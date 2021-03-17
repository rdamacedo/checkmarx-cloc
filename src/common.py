import os
import platform
from pathlib import Path

def is_accessible(path, mode='r'):
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False

    return True


def getCurrentPath():
    return os.getcwd()


def get_sysinfo():
    return platform.uname()


def getEscapeChar():
    platform = get_sysinfo().system
    if platform == "Windows":
        echar = "\\"
    elif platform == "Linux":
        echar = "/"
    elif platform == "Darwin":
        echar = "/"
    else:
        echar = ""
    return echar


# Space Char
spaceChar = " "

# Dash / Minus Char
Dash = "-"

# Dot Char
Dot = "."

# Get Escape Char According to O.S.
echar = getEscapeChar()

# Get the current directory
curPath = getCurrentPath()

# CLOC Folder and output file
outputFolder = curPath + echar + "output"
outputFileName = "checkmarx-cloc-output.txt"
output = outputFolder + echar + outputFileName


def createFolder(folder):
    try:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
    except OSError:
        text = "Could not create directory - " + folder
        print(text)
        return False

    return True


def createFile(file, msg, linebreak):
    if linebreak != 0 and linebreak != 1:
        text = "linebreak parameter can not be different from 0 or 1! - linebreak=[{}]".format(linebreak)
        print(text)
        return False

    mode = 'w'
    try:
        with open(file, mode) as f:
            if linebreak == 0:
                f.write(msg)
            elif linebreak == 1:
                f.write(msg + "\n")
    except IOError:
        text = "Could not create file - " + file
        print(text)
        return False

    return True


def appendFile(file, msg, linebreak):
    if linebreak != 0 and linebreak != 1:
        text = "linebreak parameter can not be different from 0 or 1! - linebreak=[{}]".format(linebreak)
        print(text)
        return False

    mode = 'a'
    try:
        with open(file, mode) as f:
            if linebreak == 0:
                f.write(msg)
            elif linebreak == 1:
                f.write(msg + "\n")
    except IOError:
        text = "Could not append a text into the output file - " + file
        print(text)
        return False

    return True


def doCreateFolderStructureAndFile(cFolder, cFile, cMsg, type):
    if type != 0 and type != 1:
        text = "type parameter can not be different from 0 or 1! - type=[{}]".format(type)
        print(text)
        return False

    if not createFolder(cFolder):
        return False
    else:
        f = cFolder + echar + cFile
        if not createFile(f, cMsg, type):
            return False

    return True


def validateStructureAndFile(folder, filename):
    f = folder + echar + filename

    if not os.path.exists(folder):
        return False
    else:
        if not os.path.exists(f):
            return False
        else:
            if not is_accessible(f):
                return False

    return True
