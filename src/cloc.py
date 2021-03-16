#!/usr/bin/env python3


from src.modules import emailSender, clocWrapper, gitWrapper


def main():
    msgtext = "Application starting"
    print(msgtext)

    if not gitWrapper.clone():
        print("Couldnt call clone repo, aborting")
        return False

    if not clocWrapper.call():
        print("Couldnt call callCLOC, aborting")
        return False

    if not emailSender.send():
        msgtext = "Could not sucessfully call sendEMail!"
        print(msgtext)
        return False

    msgtext = "Finished application"
    print(msgtext)


if __name__ == "__main__":
    main()
