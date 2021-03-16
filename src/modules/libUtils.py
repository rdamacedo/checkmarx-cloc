import os
import inspect
import platform
from pathlib import Path
import messages as msgcatalog

myself = lambda: inspect.stack()[1][3]


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
    uname = platform.uname()
    return uname


def getSystemEscapeChar():
    plt = get_sysinfo().system
    if plt == "Windows":
        escapeChar = "\\"
    elif plt == "Linux":
        escapeChar = "/"
    elif plt == "Darwin":
        escapeChar = "/"
    else:
        escapeChar = ""
    return escapeChar


# Space Char
spaceChar = " "

# Dash / Minus Char
Dash = "-"

# Dot Char
Dot = "."

# Get Escape Char According to O.S.
escapeChar = getSystemEscapeChar()

# Get the current directory
curPath = getCurrentPath()

# Salesforce DateFormat
salesforceDateFormat = ""  # it defaults to isoformat i.e. 2020-07-03 (YYYY = year, MM = month, DD = day)

# CLOC Folder and output file
clocOutputFolder = curPath + escapeChar + "output"
clocOutputFileName = "cloc-output.txt"
clocOutput = clocOutputFolder + escapeChar + clocOutputFileName


def createFolder(folder):
    try:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
    except OSError:
        msgtext = msgcatalog.createDirectoryError + spaceChar + " - " + folder
        print(msgtext)
        return False

    return True


def createFile(file, msg, linebreak):
    if linebreak != 0 and linebreak != 1:
        msgtext = "createFile: linebreak parameter can not be different from 0 or 1! - linebreak=[{}]".format(linebreak)
        print(msgtext)
        return False

    mode = 'w'
    try:
        with open(file, mode) as f:
            if linebreak == 0:
                f.write(msg)
            elif linebreak == 1:
                f.write(msg + "\n")
    except IOError:
        msgtext = msg.createFileError + spaceChar + " - " + file
        print(msgtext)
        return False

    return True


def appendFile(file, msg, linebreak):
    if linebreak != 0 and linebreak != 1:
        msgtext = "appendFile: linebreak parameter can not be different from 0 or 1! - linebreak=[{}]".format(linebreak)
        print(msgtext)
        return False

    mode = 'a'
    try:
        with open(file, mode) as f:
            if linebreak == 0:
                f.write(msg)
            elif linebreak == 1:
                f.write(msg + "\n")
    except IOError:
        msgtext = msg.appendFileError + spaceChar + " - " + file
        print(msgtext)
        return False

    return True


def doCreateFolderStructureAndFile(cFolder, cFile, cMsg, type):
    if type != 0 and type != 1:
        msgtext = "doCreateFolderStructureAndFile: type parameter can not be different from 0 or 1! - type=[{}]".format(
            type)
        print(msgtext)
        return False

    if not createFolder(cFolder):
        return False
    else:
        f = cFolder + escapeChar + cFile
        if not createFile(f, cMsg, type):
            return False

    return True


def validateStructureAndFile(folder, filename):
    f = folder + escapeChar + filename

    if not os.path.exists(folder):
        return False
    else:
        if not os.path.exists(f):
            return False
        else:
            if not is_accessible(f):
                return False

    return True
