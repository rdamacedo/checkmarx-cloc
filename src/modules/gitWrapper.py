import git

from src.modules.config import getConfig


def clone():
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

    repoUrl = data_dict['repoUrl']
    if repoFolder == "":
        msgtext = "Couldnt retrieve Repo URL configuration! - repoURL=[{}]".format(repoUrl)
        print(msgtext)
        return False

    repo = cloneRepoTo(repoUrl, repoFolder)
    if repo != None:
        return True
    else:
        return False


def cloneRepoTo(httpsRepo, destinationPath):
    return git.Repo.clone_from(httpsRepo, destinationPath)
