
import json
import os

from src.modules.common import curPath, echar, is_accessible


def checkStructureAndFile(folder, filename):
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

def getConfig(search_tag):
    configFileName = "settings.json"
    configFolderPath = curPath
    if checkStructureAndFile(configFolderPath, configFileName):
        f = configFolderPath + echar + configFileName
        try:
            with open(f, 'r') as config:
                data = json.load(config)
                datadict = data[search_tag][0]

        except Exception:
            text = "Error reading file - " + f
            print(text)
            return None

    return datadict

def checkSMTPConfig(data):

    server = data['server']
    if server == "":
        text = "Could not get SMTP server configuration! - smtpServer=[{}]".format(server)
        print(text)
        return False

    port = data['port']
    if port == "":
        text = "Could not get SMTP port configuration! - smtpPort=[{}]".format(port)
        print(text)
        return False

    SSL = data['SSL']
    if SSL == "" or (SSL.upper() != "YES" and SSL.upper() != "NO" and SSL.upper() != "TRUE" and SSL.upper() != "FALSE"):
        text = "Error on SSL configuration! - SSL=[{}]".format(SSL)
        print(text)
        return False

    sender = data['sender']
    if sender == "":
        text = "Error on Sender configuration! - sender=[{}]".format(sender)
        print(text)
        return False

    recipient = data['recipient']
    if recipient == "":
        text = "Error on Recipient configuration! - recipient=[{}]".format(recipient)
        print(text)
        return False

    subject = data['subject']
    if subject == "":
        text = "Error on Subject configuration! - subject=[{}]".format(subject)
        print(text)
        return False

    username = data['username']
    if username == "":
        text = "Error on Username configuration! - username=[{}]".format(username)
        print(text)
        return False

    password = data['password']
    if password == "":
        text = "Error on Password configuration! - password=[{}]".format(password)
        print(text)
        return False

    text = "SMTP={} - Port={} - SSL={} - Sender={} - Recipient={} - Subject={}".format(server, port, SSL, sender, recipient, subject)
    print(text)

    return True
