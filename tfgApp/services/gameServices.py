import random
import string
from tfgApp.models import Game
from tfgApp.repositories import gameRepository


def gameToJson(game, user):
    json = {
        "Name": game.name,
        "Code": game.code,
        "Map": game.map,
        "ChipList": game.chipList,
        "Users": {user[0]: user[1]}
    }
    return json


def createGame(name, mapId, user):
    code = generateRandomId()
    gameDB = Game(name, code, mapId, [])
    gameJson = gameToJson(gameDB, user)
    message, id = gameRepository.create(gameJson)
    return message, id


def get(id):
    game = gameRepository.get(id)
    return game


def getProperty(id, propierty):
    valueFromPropierty = gameRepository.getProperty(id, propierty)
    return valueFromPropierty


def getGameIdFromCode(gameCode):
    gamesDict = gameRepository.getAllGamesIdsAndCodes()
    gameId = None
    if gameCode in gamesDict.keys():
        gameId = gamesDict[gameCode]
    return gameId


def getAllGamesIdsAndCodes():
    gamesDict = gameRepository.getAllGamesIdsAndCodes()
    return gamesDict


def generateRandomId():  ##TODO: añadir un sistema para verificar que no existe ya ese ID
    randomId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    return randomId


def addUserToGame(gameId, userId):
    gameRepository.addUserToGame(gameId, userId)


def testCreate():
    game1 = Game("autoTestGame", "01", "autoTestMap", "autoTestChipList")
    game1Json = gameToJson(game1)
    message = gameRepository.create(game1Json)
    return message


def testUpdate():
    game1 = Game("autoTestGame", "01", "autoTestMap", "autoTestChipList")
    game1.code = 2
    game1Json = gameToJson(game1)
    message = gameRepository.update(game1Json)
    return message


def testDelete():
    game1 = Game("autoTestGame", "01", "autoTestMap", "autoTestChipList")
    game1Json = gameToJson(game1)
    message = gameRepository.delete(game1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
