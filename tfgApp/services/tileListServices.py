from tfgApp.models import TileList
from tfgApp.repositories import tileListRepository


def tileListToJson(tileList):
    position = {pos: name for pos, name in tileList.position}
    json = {
            "Name": tileList.name,
            "Position": position
        }
    return json


def testCreate():
    tileList1 = TileList("testTileListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    tileList1Json = tileListToJson(tileList1)
    message = tileListRepository.create(tileList1Json)
    return message


def testUpdate():
    tileList1 = TileList("testTileListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    tileList1.position = [("1-1", "ForestTree"), ("2-1", "SimpleGrass"), ("2-3", "ForestTree")]
    tileList1Json = tileListToJson(tileList1)
    message = tileListRepository.update(tileList1Json)
    return message


def testDelete():
    tileList1 = TileList("testTileListName2", [("1-1", "ForestTree"), ("2-1", "ForestTree"), ("2-3", "ForestTree")])
    tileList1Json = tileListToJson(tileList1)
    message = tileListRepository.delete(tileList1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
