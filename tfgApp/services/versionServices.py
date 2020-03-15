from tfgApp.models import Version
from tfgApp.repositories import versionRepository


def versionToJson(version):
    json = {
            "Name": version.name,
            "Map": version.map,
            "Order": version.order,
            "TileList": version.tileList
        }
    return json


def testCreate():
    version1 = Version("testMapName_1", "testMapName", "1", "testTileListName")
    version1Json = versionToJson(version1)
    message = versionRepository.create(version1Json)
    return message


def testUpdate():
    version1 = Version("testMapName_1", "testMapName", "1", "testTileListName")
    version1.tileList = "testTileListNameEdited"
    version1Json = versionToJson(version1)
    message = versionRepository.update(version1Json)
    return message


def testDelete():
    version1 = Version("testMapName_1", "testMapName", "1", "testTileListName")
    version1Json = versionToJson(version1)
    message = versionRepository.delete(version1Json)
    return message


def test():
    print("== Caso positivo crear == ", testCreate())
    print("== Caso negativo crear == ", testCreate())
    print("== Caso positivo editar == ", testUpdate())
    print("== Caso positivo eliminar == ", testDelete())
