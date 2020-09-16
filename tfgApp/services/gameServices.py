from tfgApp.models import Game
from tfgApp.repositories import gameRepository


def gameToJson(game):
    json = {
            "GameName" : game.name,
            "GameCode" : game.code,
            "Map" : game.map,
            "ChipList" : game.chipList
        }
    return json


def get(id):
    game = gameRepository.get(id)
    return game


def getProperty(id, propierty):
    valueFromPropierty = gameRepository.getProperty(id, propierty)
    return valueFromPropierty


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