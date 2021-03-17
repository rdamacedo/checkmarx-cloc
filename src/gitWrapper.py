import git

from settings import getSettings


def clone():
    data = getSettings('repository')
    if data == None:
        text = "Couldnt retrieve configuration. - data=[{}]".format(data)
        print(text)
        return False

    repoFolder = data['repoFolder']
    if repoFolder == "":
        text = "Couldnt retrieve configuration! - repoFolder=[{}]".format(repoFolder)
        print(text)
        return False

    repoUrl = data['repoUrl']
    if repoFolder == "":
        text = "Couldnt retrieve configuration! - repoURL=[{}]".format(repoUrl)
        print(text)
        return False

    repo = cloneRepoTo(repoUrl, repoFolder)
    if repo != None:
        return True
    else:
        return False


def cloneRepoTo(httpsRepo, destinationPath):
    return git.Repo.clone_from(httpsRepo, destinationPath)
