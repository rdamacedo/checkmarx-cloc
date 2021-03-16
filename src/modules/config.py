
import json
import os

from src.modules.libUtils import curPath, escapeChar, spaceChar, is_accessible


def checkStructureAndFile(folder, filename):
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

def getConfig(search_tag):
    configFileName = "config.json"
    configFolderPath = curPath + escapeChar + "config"
    if checkStructureAndFile(configFolderPath, configFileName):
        f = configFolderPath + escapeChar + configFileName
        try:
            with open(f, 'r') as config:
                data = json.load(config)
                data_dict = data[search_tag][0]

        except Exception:
            msgtext = "Error reading file" + spaceChar + " - " + f
            print(msgtext)
            return None

    return data_dict

def checkEMailConfig(data_dict):

    smtpServer = data_dict['SMTPServer']
    if smtpServer == "":
        msgtext = "Could not get SMTP server configuration! - smtpServer=[{}]".format(smtpServer)
        print(msgtext)
        return False

    smtpPort = data_dict['SMTPPort']
    if smtpPort == "":
        msgtext = "Could not get SMTP port configuration! - smtpPort=[{}]".format(smtpPort)
        print(msgtext)
        return False

    useSSL = data_dict['useSSL']
    if (useSSL == "" or (useSSL != "YES" and useSSL != "NO")):
        msgtext = "Error while getting SSL configuration! - useSSL=[{}]".format(useSSL)
        print(msgtext)
        return False

    sender = data_dict['sender']
    if sender == "":
        msgtext = "Could not get Sender configuration! - sender=[{}]".format(sender)
        print(msgtext)
        return False

    senderName = data_dict['senderName']
    if senderName == "":
        msgtext = "Could not get Sender Name configuration! - senderName=[{}]".format(senderName)
        print(msgtext)
        return False

    receiver = data_dict['receiver']
    if receiver == "":
        msgtext = "Could not get Receiver configuration! - receiver=[{}]".format(receiver)
        print(msgtext)
        return False

    receiverName = data_dict['receiverName']
    if receiverName == "":
        msgtext = "Could not get Receiver Name configuration! - receiverName=[{}]".format(receiverName)
        print(msgtext)
        return False

    subject = data_dict['subject']
    if subject == "":
        msgtext = "Could not get Subject configuration! - subject=[{}]".format(subject)
        print(msgtext)
        return False

    username = data_dict['username']
    if username == "":
        msgtext = "Could not get Username configuration! - username=[{}]".format(username)
        print(msgtext)
        return False

    password = data_dict['password']
    if password == "":
        msgtext = "Could not get Password configuration! - password=[{}]".format(password)
        print(msgtext)
        return False

    msgtext = "SMTPServer=[{}] - Port=[{}] - UserSSL=[{}] - Sender=[{}] - Receiver=[{}] - Subject=[{}]".format(smtpServer, smtpPort, useSSL, sender, receiver, subject)
    print(msgtext)

    return True