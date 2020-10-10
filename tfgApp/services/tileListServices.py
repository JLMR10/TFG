from tfgApp.models import TileList
from tfgApp.repositories import tileListRepository


def tileListToJson(tileList):
    position = {pos+"_": name for pos, name in tileList.position.items()}
    json = {
            "Position": position
        }
    return json


def create(json):
    message, tileListId = tileListRepository.create(json)
    return message, tileListId


def get(id):
    tileList = tileListRepository.get(id)
    return tileList


def getPropierty(id, propierty):
    valueFromPropierty = tileListRepository.getPropierty(id, propierty)
    return valueFromPropierty


def mergeAndCreateTileList(tileListsIds):
    tileLists = [getPropierty(id, "Position") for id in tileListsIds]
    mergedTileList = {}
    for tileList in tileLists:
        for position, tile in tileList.items():
            ##position = position.replace("_", "")
            mergedTileList[position] = tile
    mergedTileListObj = TileList(mergedTileList)
    mergedTileListJson = tileListToJson(mergedTileListObj)
    _, mergedTileListId = tileListRepository.create(mergedTileListJson)
    return mergedTileListId


def mergeTileList(tileListsIds):
    tileLists = [getPropierty(id, "Position") for id in tileListsIds]
    mergedTileList = {}
    for tileList in tileLists:
        for position, tile in tileList.items():
            mergedTileList[position.split("_")[0]] = tile
    return mergedTileList


def testCreate():
    tileList1 = TileList("testTileListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    tileList1Json = tileListToJson(tileList1)
    message, _ = tileListRepository.create(tileList1Json)
    return message


def testUpdate():
    tileList1 = TileList("testTileListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    tileList1.position = [("1-1", "ForestTree"), ("2-1", "SimpleGrass"), ("2-3", "ForestTree")]
    tileList1Json = tileListToJson(tileList1)
    message = tileListRepository.update(tileList1Json)
    return message,_


def testDelete():
    tileList1 = TileList("testTileListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    tileList1Json = tileListToJson(tileList1)
    message = tileListRepository.delete(tileList1Json)
    return message,_


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
