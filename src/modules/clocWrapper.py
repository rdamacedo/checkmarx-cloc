import os
import subprocess

from src.modules.config import getConfig
from src.modules.libUtils import clocOutputFolder, createFolder, spaceChar, clocOutput


def call():
    data_dict = getConfig('repo_config')
    if data_dict == None:
        msgtext = "Couldnt retrieve Config. - data_dict=[{}]".format(data_dict)
        print(msgtext)
        return False

    repoFolder = data_dict['localRepoFolder']
    if repoFolder == "":
        msgtext = "Couldnt retrieve Repo Folder configuration! - repoFolder=[{}]".format(repoFolder)
        print(msgtext)
        return False

    msgtext = "RepoFolder=[{}]".format(repoFolder)
    print(msgtext)

    cloc_bin = "../libs/cloc/cloc-188.pl"

    if not os.path.exists(clocOutputFolder):
        if not createFolder(clocOutputFolder):
            msgtext = "Create folder error " + spaceChar + " - " + clocOutputFolder
            print(msgtext)
            return False

    with open(clocOutput, 'wb', 0) as f:
        rescode = subprocess.call(["perl", cloc_bin, repoFolder], stdout=f)
        if rescode != 0:
            msgtext = "Could not sucessfully call CLOC artifact! - ResultCode=[{}]".format(rescode)
            print(msgtext)
            return False

    return True
