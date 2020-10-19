from tfgApp.models import User
from tfgApp.repositories import userRepository


def userToJson(user):
    maps = {map: True for map in user.maps}
    games = {game: True for game in user.games}
    json = {
            "Name": user.name,
            "Email": user.email,
            "Password": user.password,
            "Maps": maps,
            "Games": games
        }
    return json


def createUser(id, name, email):
    userDB = User(name, email, "", [], [])
    userJson = userToJson(userDB)
    message = userRepository.create(userJson, id)
    return message


def getMaps(id):
    userRepository.getMaps(id)


def addMap(userId, mapId):
    userRepository.addMap(userId, mapId)


def addGameToUser(userId, gameId, gameName):
    userRepository.addGameToUser(userId, gameId, gameName)


def getPropierty(id, propierty):
    valueFromPropierty = userRepository.getPropierty(id, propierty)
    return valueFromPropierty


def update(id, value, propierty):
    return userRepository.update(id, value, propierty)


def getIdAndNamesFromUsersList(usersList):
    usersNamesList = {}
    for userId in usersList:
        usersNamesList[userId] = userRepository.getPropierty(userId, "Name")
    return usersNamesList


def testCreate():
    user1 = User("Guille", "Guille@pueba.com", "JGJG75F", ["DefaultMap1", "DefaultMap2", "DefaultMap3"], ["testGame"])
    user1Json = userToJson(user1)
    message = userRepository.create(user1Json)
    return message


def testUpdate():
    user1 = User("Guille", "Guille@pueba.com", "JGJG75F", ["DefaultMap1", "DefaultMap2", "DefaultMap3"], ["testGame"])
    user1.email = "232323@prueba.com"
    user1Json = userToJson(user1)
    message = userRepository.update(user1Json)
    return message


def testDelete():
    user1 = User("Guille", "Guille@pueba.com", "JGJG75F", ["DefaultMap1", "DefaultMap2", "DefaultMap3"], ["testGame"])
    user1Json = userToJson(user1)
    message = userRepository.delete(user1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
