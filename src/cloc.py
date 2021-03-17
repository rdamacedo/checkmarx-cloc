#!/usr/bin/env python3

// Application Entry Point

from src.modules import emailSender, clocWrapper, gitWrapper

def main():
    print("Application Initialization")

    if not gitWrapper.clone():
        print("Couldnt call clone repo, aborting")
        return False

    if not clocWrapper.call():
        print("Couldnt call CLOC, aborting")
        return False

    if not emailSender.send():
        print("Could not sucessfully call send EMail function!")
        return False

    print("Finished application")


if __name__ == "__main__":
    main()
