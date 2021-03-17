import os
import subprocess

from src.modules.config import getConfig
from src.modules.common import outputFolder, createFolder, spaceChar, output


def call():
    data = getConfig('repository')
    if data == None:
        text = "Couldnt retrieve configuration. - data=[{}]".format(data)
        print(text)
        return False

    repoFolder = data['repoFolder']
    if repoFolder == "":
        text = "Couldnt retrieve configuration! - repoFolder=[{}]".format(repoFolder)
        print(text)
        return False

    text = "RepoFolder=[{}]".format(repoFolder)
    print(text)

    cloc_bin = "../libs/cloc/cloc-188.pl"

    if not os.path.exists(outputFolder):
        if not createFolder(outputFolder):
            text = "Create folder error  - " + outputFolder
            print(text)
            return False

    with open(output, 'wb', 0) as f:
        result_code = subprocess.call(["perl", cloc_bin, repoFolder], stdout=f)
        if result_code != 0:
            text = "Error calling CLOC artifact! - ResultCode=[{}]".format(result_code)
            print(text)
            return False

    return True
