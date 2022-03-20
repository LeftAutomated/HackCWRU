import dbms


def checkUserExist(discordId):
    if dbms.userSearch(discordId):
        return True
    else:
        return False

def checkWordExist(discordId, message):
    message = message.split()
    print(message)

    for word in message:
        if dbms.wordSearchPositive(word):
            dbms.userUpdateHappy(discordId, dbms.userSearch(discordId)[0][2] + 1)
        if dbms.wordSearchNegative(word):
            dbms.userUpdateHappy(discordId, dbms.userSearch(discordId)[0][3] + 1)
        else:
            return False
