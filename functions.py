import dbms


def checkUserExist(discordId):
    if dbms.userSearch(discordId):
        return True
    else:
        return False

def checkWordExist(discordId, message):
    message = message.split()

    for word in message:
        if dbms.wordSearchPositive(word):
            dbms.userUpdateHappy(discordId, dbms.userSearch(discordId)[0][2] + 1)
        if dbms.wordSearchNegative(word):
            dbms.userUpdateSad(discordId, dbms.userSearch(discordId)[0][3] + 1)
