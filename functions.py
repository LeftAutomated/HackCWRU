import dbms


def checkUserExist(discordId):
    if dbms.userSearch(discordId):
        return True
    else:
        return False
